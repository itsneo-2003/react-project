Password rotation for cloud-native Entra ID user accounts can be implemented using Microsoft Graph REST APIs.
Authentication can be done using OAuth2 client-credentials flow (client-id and client-secret).
The password can be rotated by calling PATCH /v1.0/users/{id} with passwordProfile payload.
This approach does not rely on Graph SDKs or certificate-based authentication and fully aligns with REST-based integration.
