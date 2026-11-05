# Handoff: React Application Authentication with SharePoint Online

## Purpose

This document captures the conversation about querying SharePoint List
data from a React application and the authentication architecture
discussed, so another LLM can continue the work without needing the
original chat.

## User's goal

The user is exploring a React application/dashboard that reads data from
existing SharePoint Online lists. The lists mentioned in the broader
project context are:

-   **Baseline** --- desired/configuration baseline values.
-   **Transaction** --- records of configuration reviews/runs, including
    configuration names/values, review identifiers, timestamps, and
    compliance status.
-   **Automation Tracker** --- a tracker row containing information such
    as the last run/review.

The likely use case is a dashboard that displays configuration
compliance information sourced from these SharePoint lists.

The user first asked whether SharePoint list data can be queried from
React using REST APIs or other APIs. The answer was yes, using either
Microsoft Graph API or SharePoint REST API. The recommended approach was
React + MSAL + Microsoft Graph.

The user then asked to dig deeper into authentication. The discussion
focused on Microsoft Entra ID, OAuth 2.0, MSAL, delegated permissions,
app registration, access tokens, and calling Microsoft Graph from React.

------------------------------------------------------------------------

## 1. API choices

### Option A: Microsoft Graph API (recommended)

Example endpoint to retrieve SharePoint list items:

``` http
GET https://graph.microsoft.com/v1.0/sites/{site-id}/lists/{list-id}/items?expand=fields
```

To request selected fields:

``` http
GET https://graph.microsoft.com/v1.0/sites/{site-id}/lists/{list-id}/items?expand=fields(select=ConfigName,ConfigValue,Status)
```

Graph can also be used to discover the site and list IDs:

``` http
GET https://graph.microsoft.com/v1.0/sites/{hostname}:/sites/{site-name}
```

``` http
GET https://graph.microsoft.com/v1.0/sites/{site-id}/lists
```

``` http
GET https://graph.microsoft.com/v1.0/sites/{site-id}/lists/{list-id}/items?expand=fields
```

Official documentation: - List items:
https://learn.microsoft.com/en-us/graph/api/listitem-list?view=graph-rest-1.0 -
Microsoft Graph API generally: https://learn.microsoft.com/en-us/graph/

### Option B: SharePoint REST API

Example:

``` http
GET https://yourtenant.sharepoint.com/sites/yoursite/_api/web/lists/getbytitle('Baseline')/items
```

Example React fetch:

``` javascript
const response = await fetch(
  "https://yourtenant.sharepoint.com/sites/yoursite/_api/web/lists/getbytitle('Baseline')/items",
  {
    headers: {
      Accept: "application/json;odata=nometadata"
    }
  }
);

const data = await response.json();
console.log(data.value);
```

Authentication is still required. For a new React application, Microsoft
Graph was recommended as the preferred integration.

------------------------------------------------------------------------

## 2. Authentication architecture recommended

Recommended stack:

-   React frontend
-   Microsoft Entra ID app registration
-   MSAL (`@azure/msal-browser` and `@azure/msal-react`)
-   Microsoft Graph API
-   SharePoint Online

High-level flow:

1.  User opens the React application.
2.  React checks whether the user is authenticated.
3.  MSAL initiates sign-in with Microsoft Entra ID.
4.  The user signs in with their organisational Microsoft 365 account.
5.  Entra ID authenticates the user and issues tokens through the OAuth
    2.0 flow.
6.  MSAL obtains an access token intended for Microsoft Graph.
7.  React sends the access token in the HTTP `Authorization: Bearer`
    header.
8.  Microsoft Graph validates the token and permissions, then accesses
    SharePoint.
9.  SharePoint returns the list data the user is authorised to access.

Important distinction: - An **ID token** provides identity information
about the signed-in user. - An **access token** authorises access to a
protected API such as Microsoft Graph. - For Graph requests, obtain an
access token for Microsoft Graph, not merely an ID token.

For browser-based single-page applications, use **OAuth 2.0
Authorization Code Flow with PKCE**. Do not use the implicit flow for a
new implementation.

Official references: - React MSAL quickstart:
https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-single-page-app-react-sign-in -
Authorization code flow:
https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow -
MSAL authentication flows:
https://learn.microsoft.com/en-us/entra/identity-platform/msal-authentication-flows

------------------------------------------------------------------------

## 3. Delegated permissions vs application permissions

### Delegated permissions

The application accesses data on behalf of a signed-in user.

For example: - Sarvesh signs in to the React dashboard. - MSAL obtains a
Graph access token for that user. - Graph checks the granted delegated
permissions. - SharePoint access is also constrained by the signed-in
user's own SharePoint permissions.

This is the recommended model for an interactive user-facing dashboard.

### Application permissions

The application accesses data using its own identity, without a
signed-in user.

This is typically used for: - Background services - Scheduled jobs -
Server-to-server automation

A React-only browser application should not use application permissions
directly. Application permissions require a confidential client,
typically a backend service, and credentials such as a certificate or
secret must never be embedded in browser code.

### Comparison

  -----------------------------------------------------------------------
  Feature                 Delegated permission    Application permission
  ----------------------- ----------------------- -----------------------
  User sign-in required   Yes                     No

  Access identity         Signed-in user          Application/service
                                                  principal

  Suitable for React-only Yes                     No
  SPA                                             

  Backend generally       No                      Yes
  needed                                          

  User's SharePoint       Yes                     No; app's granted
  permissions apply                               permissions govern
                                                  access

  Typical use             Interactive dashboard   Background automation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 4. Entra ID app registration setup

Navigate to Microsoft Entra admin center:

https://entra.microsoft.com/

Go to:

**Identity → Applications → App registrations → New registration**

Suggested initial configuration:

  -----------------------------------------------------------------------
  Setting                             Value
  ----------------------------------- -----------------------------------
  Name                                SharePoint React Dashboard

  Supported account types             Accounts in this organizational
                                      directory only (single tenant),
                                      assuming only the user's
                                      organisation should access it

  Platform                            Single-page application (SPA)

  Development redirect URI            `http://localhost:5173` (for a Vite
                                      React development server)
  -----------------------------------------------------------------------

After registration, note: - **Application (client) ID** - **Directory
(tenant) ID**

Then go to **Authentication** and confirm the SPA platform and redirect
URI are configured.

Do not configure the React SPA as a confidential Web application. A
browser-based SPA is a public client and cannot safely keep a client
secret.

For production, add the actual deployed application URL as a separate
SPA redirect URI. Ensure redirect URIs match exactly.

------------------------------------------------------------------------

## 5. Graph API permissions

Under:

**App registrations → SharePoint React Dashboard → API permissions → Add
a permission → Microsoft Graph → Delegated permissions**

Suggested initial permissions for a read-only SharePoint dashboard:

-   `User.Read` --- read the signed-in user's basic profile.
-   `Sites.Read.All` --- read SharePoint site/list content accessible
    under the delegated permission model.

`Sites.Read.All` is a broad permission. It should only be requested if
it is acceptable under the organisation's security policy. An
administrator may need to grant admin consent, depending on tenant
consent settings.

Important: - API permission consent does **not** automatically grant the
user access to all SharePoint sites. - With delegated access, the
signed-in user must also have the relevant SharePoint site/list
permissions. - Do not request write or full-control permissions for a
read-only dashboard. - If a future feature needs to update lists,
evaluate the narrowest suitable write permission and obtain the
necessary consent. - For app-only access in a backend scenario,
investigate `Sites.Selected` to restrict the application to explicitly
authorised sites. This is not a substitute for carefully designing
delegated user access.

Official references: - List items API permissions:
https://learn.microsoft.com/en-us/graph/api/listitem-list?view=graph-rest-1.0 -
Selected permissions overview:
https://learn.microsoft.com/en-us/graph/permissions-selected-overview

------------------------------------------------------------------------

## 6. Install MSAL packages

In the React project:

``` bash
npm install @azure/msal-browser @azure/msal-react
```

Responsibilities:

  -----------------------------------------------------------------------
  Package                             Responsibility
  ----------------------------------- -----------------------------------
  `@azure/msal-browser`               Browser authentication, token
                                      acquisition, token cache

  `@azure/msal-react`                 React provider, hooks, and
                                      components for authentication state
  -----------------------------------------------------------------------

Useful MSAL React APIs: - `MsalProvider` - `useMsal()` -
`useIsAuthenticated()` - `useAccount()`

------------------------------------------------------------------------

## 7. Example implementation discussed

These are starter examples, not a complete production-ready application.
The next LLM should validate the current MSAL package APIs and improve
error handling, account selection, initialization, and token handling
before treating this as deployable code.

### `src/authConfig.js`

``` javascript
export const msalConfig = {
  auth: {
    clientId: "YOUR_CLIENT_ID",
    authority: "https://login.microsoftonline.com/YOUR_TENANT_ID",
    redirectUri: "http://localhost:5173"
  },
  cache: {
    cacheLocation: "sessionStorage"
  }
};

export const loginRequest = {
  scopes: ["User.Read", "Sites.Read.All"]
};
```

Replace the placeholders with the values from the Entra app
registration.

`sessionStorage` was chosen as a conservative browser cache option for
the example. The storage choice should be assessed against the
application's user experience and security requirements.

### `src/msalInstance.js`

``` javascript
import { PublicClientApplication } from "@azure/msal-browser";
import { msalConfig } from "./authConfig";

export const msalInstance = new PublicClientApplication(msalConfig);
```

### `src/main.jsx`

``` jsx
import React from "react";
import ReactDOM from "react-dom/client";
import { MsalProvider } from "@azure/msal-react";

import App from "./App";
import { msalInstance } from "./msalInstance";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <MsalProvider instance={msalInstance}>
      <App />
    </MsalProvider>
  </React.StrictMode>
);
```

Check the installed MSAL Browser version's initialization requirements.
Current versions may require explicitly awaiting `initialize()` before
invoking other MSAL APIs. Ensure initialization is completed before
rendering or using the instance.

### `src/components/Login.jsx`

``` jsx
import { useMsal } from "@azure/msal-react";
import { loginRequest } from "../authConfig";

function Login() {
  const { instance } = useMsal();

  const handleLogin = async () => {
    await instance.loginPopup(loginRequest);
  };

  return (
    <button onClick={handleLogin}>
      Login with Microsoft
    </button>
  );
}

export default Login;
```

Popup authentication is shown here. Redirect authentication is also
supported. Choose one interaction pattern and handle its response
consistently.

### Acquiring a Graph access token

The earlier example used the silent-first pattern:

``` javascript
import { InteractionRequiredAuthError } from "@azure/msal-browser";

export async function getAccessToken(instance, account) {
  const request = {
    scopes: ["Sites.Read.All"],
    account
  };

  try {
    const response = await instance.acquireTokenSilent(request);
    return response.accessToken;
  } catch (error) {
    if (error instanceof InteractionRequiredAuthError) {
      const response = await instance.acquireTokenPopup(request);
      return response.accessToken;
    }

    throw error;
  }
}
```

Concept: 1. Try `acquireTokenSilent()` first. 2. MSAL checks its cache
and attempts to renew/acquire a token without user interaction. 3. If
interaction is required, use an interactive fallback such as
`acquireTokenPopup()` or redirect. 4. Do not repeatedly prompt the user
unnecessarily. 5. Handle network errors, consent errors, expired
sessions, and other MSAL errors separately in a robust implementation.

The account should be selected from the MSAL accounts available in the
app. Do not assume that `accounts[0]` is always the intended account in
multi-account scenarios.

### Calling Graph for list items

``` javascript
import { getAccessToken } from "./sharepointService";

export async function getSharePointList(instance, account, siteId, listId) {
  const accessToken = await getAccessToken(instance, account);

  const url =
    `https://graph.microsoft.com/v1.0/sites/${siteId}/lists/${listId}/items?expand=fields`;

  const response = await fetch(url, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      Accept: "application/json"
    }
  });

  if (!response.ok) {
    throw new Error(`Graph API error: ${response.status}`);
  }

  const data = await response.json();
  return data.value;
}
```

The returned list item fields are available under each item's `fields`
property.

For production, also consider: - Graph pagination via
`@odata.nextLink`. - `$select`/field selection to reduce payload size. -
Loading/error states in React. - Retry/backoff for throttling (`429`)
and transient failures. - Avoiding repeated site/list discovery if IDs
are stable. - Validating and encoding URL path components. - Never
logging access tokens.

------------------------------------------------------------------------

## 8. Security guidance

-   Never put a client secret, certificate private key, or other
    confidential credential in React code, `.env` variables bundled into
    the frontend, or browser storage.
-   Client IDs and tenant IDs are identifiers, not secrets.
-   Do not log access tokens or expose them in UI/debug output.
-   Use MSAL for authentication and token acquisition; do not implement
    OAuth token handling manually.
-   Use Authorization Code Flow with PKCE for the SPA.
-   Request only the permissions the app needs.
-   Use delegated permissions for a user-facing dashboard unless a
    clearly justified backend/app-only requirement exists.
-   Enforce access on the API/SharePoint side; hiding UI elements is not
    security.
-   If the app later needs app-only permissions, put that logic in a
    secure backend and store credentials in an appropriate
    secret/certificate store, such as Azure Key Vault.
-   Use HTTPS in deployed environments.
-   Configure exact redirect URIs and appropriate logout URLs.
-   Consider Conditional Access and the organisation's consent policies.

------------------------------------------------------------------------

## 9. Suggested project structure

``` text
src/
│
├── auth/
│   ├── authConfig.js
│   └── msalInstance.js
│
├── services/
│   └── sharepointService.js
│
├── components/
│   ├── Login.jsx
│   ├── Dashboard.jsx
│   ├── Baseline.jsx
│   ├── Transaction.jsx
│   └── Tracker.jsx
│
├── App.jsx
└── main.jsx
```

------------------------------------------------------------------------

## 10. Suggested implementation plan

Recommended incremental path:

1.  Create a single-tenant Entra app registration.
2.  Add a SPA redirect URI for local development.
3.  Add the minimum required delegated Graph permissions.
4.  Obtain admin consent if the tenant requires it.
5.  Install and configure MSAL.
6.  Implement sign-in and sign-out.
7.  Display the signed-in account.
8.  Acquire a Graph token silently, with interactive fallback only when
    needed.
9.  Call Graph to discover the SharePoint site and lists.
10. Retrieve the Baseline list and render it in React.
11. Add Transaction and Automation Tracker data.
12. Add filtering/search and compliance visualisations.
13. Only after read access works, consider list updates and any backend
    automation.

The initial target should be a **read-only dashboard** using delegated
`Sites.Read.All`.

------------------------------------------------------------------------

## 11. Open decisions / questions for the next stage

These were asked in the conversation but the user has not yet answered
them:

### Who will use the application?

-   Only the user?
-   Everyone in the organisation?
-   A selected group of employees?

This affects the supported account type, assignment/access strategy,
consent, and rollout.

### What operations should it support?

-   Read-only SharePoint access?
-   Read and update SharePoint lists?
-   Read/update and trigger configuration compliance automation?

This affects the permission scope and whether a backend is needed.

### Where will it run?

-   Locally on the user's laptop?
-   Hosted on Azure?
-   Hosted on an internal company server?

This affects redirect URIs, hosting, deployment, and security
configuration.

### Other implementation details to confirm

-   SharePoint tenant hostname and site path.
-   Whether the user can register applications or needs an Entra
    administrator.
-   Whether the organisation permits user consent or requires admin
    consent.
-   Whether users already have read access to the target SharePoint
    lists.
-   Whether the dashboard should use only Graph or has a requirement to
    use SharePoint REST.

Do not ask the user to repeat details already present in this handoff.
Ask only for the next genuinely necessary decision.

------------------------------------------------------------------------

## 12. Relevant background about the user's existing SharePoint project

The user has previously worked on a Microsoft Entra configuration
monitoring workflow involving SharePoint lists:

-   **Baseline list:** desired feature/configuration values; intended to
    have no duplicate controls.
-   **Transaction list:** append a new set of rows for each review/run
    rather than updating old transaction rows.
-   **Automation Tracker:** a single tracker row, including `LastRun`,
    review count, and last-run date/time.
-   Transaction records include fields such as `ConfigName`,
    `ConfigValue`, `Review`, `LastRunDateTime`, and `Status`.
-   The user has worked with PowerShell, Microsoft Graph, SharePoint
    lists, and Power Automate.
-   The user has previously been advised to avoid making a separate
    Graph call for every control and instead cache baseline/current
    values in hash tables where appropriate.
-   The React application being discussed is a potential way to display
    the existing SharePoint data in a dashboard.

This background may help shape the dashboard data model, but do not
assume the React app should execute the existing PowerShell compliance
logic unless the user explicitly asks for that. The current conversation
focused on authentication and reading SharePoint data.

------------------------------------------------------------------------

## 13. Key recommendation

Start with:

**Single-tenant React SPA + MSAL + delegated Microsoft Graph
permissions + read-only SharePoint access.**

Use `Sites.Read.All` only if the organisation approves its scope.
Confirm the user's actual access to the relevant SharePoint site. Get
the Baseline list loading successfully before expanding the app.

Keep app-only access and client credentials out of the browser. If
future requirements call for unattended automation or application-level
access, design a separate secure backend rather than embedding secrets
in React.
