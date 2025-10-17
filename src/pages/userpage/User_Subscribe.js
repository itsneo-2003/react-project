import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './User_Subscribe.css';

const User_Subscribe = () => {
  
  const availableGroups = [
    { 
      id: 1, 
      name: 'Credit Card Group', 
      description: 'Access credit card reports, analytics, and customer insights',
      icon: '💳' 
    },
    { 
      id: 2, 
      name: 'Risk Compliance Group', 
      description: 'Regulatory compliance reports and risk assessment documents',
      icon: '⚖️' 
    },
    { 
      id: 3, 
      name: 'Loan Group', 
      description: 'Loan portfolio management and approval metrics',
      icon: '🏦' 
    },
    { 
      id: 4, 
      name: 'Investment Group', 
      description: 'Investment strategies, market analysis, and portfolio reports',
      icon: '📈' 
    },
    { 
      id: 5, 
      name: 'Customer Service Group', 
      description: 'Customer satisfaction surveys and service quality reports',
      icon: '👥' 
    },
    { 
      id: 6, 
      name: 'Savings Account Group', 
      description: 'Savings account analytics and customer retention data',
      icon: '💰' 
    },
    { 
      id: 7, 
      name: 'Fraud Detection Group', 
      description: 'Fraud prevention reports and security incident analysis',
      icon: '🔒' 
    },
    { 
      id: 8, 
      name: 'Digital Banking Group', 
      description: 'Mobile and online banking usage statistics and trends',
      icon: '📱' 
    },
    { 
      id: 9, 
      name: 'Treasury Group', 
      description: 'Treasury operations, liquidity management, and cash flow reports',
      icon: '🏛️' 
    },
    { 
      id: 10, 
      name: 'Operations Group', 
      description: 'Operational efficiency metrics and process improvement reports',
      icon: '⚙️' 
    },
    { 
      id: 11, 
      name: 'Mortgage Group', 
      description: 'Mortgage lending reports and housing market analysis',
      icon: '🏠' 
    },
    { 
      id: 12, 
      name: 'Wealth Management Group', 
      description: 'High net worth client portfolios and wealth advisory reports',
      icon: '💎' 
    },
  ];

  const [searchQuery, setSearchQuery] = useState('');

  
  const filteredGroups = availableGroups.filter(group =>
    group.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const handleSubscribe = (groupId, groupName) => {
  
    console.log('Subscribing to group:', groupId);
    alert(`Subscription request sent for: ${groupName}`);
  };

  return (
    <div className="subscribe-container">
      
      <div className="subscribe-header">
        <h2>Explore Groups</h2>
        <p>Browse and subscribe to groups to access their reports</p>
      </div>

      
      <div className="subscribe-search">
        <div className="input-group subscribe-search-box">
          <span className="input-group-text">
            <i className="bi bi-search"></i>
          </span>
          <input 
            type="text" 
            className="form-control" 
            placeholder="Search groups by name..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>
      </div>

      
      <div className="subscribe-results-count">
        <small>
          Showing {filteredGroups.length} of {availableGroups.length} groups
        </small>
      </div>

      
      <div className="row g-4">
        {filteredGroups.length > 0 ? (
          filteredGroups.map((group) => (
            <div key={group.id} className="col-md-6 col-lg-4">
              <div className="card shadow-sm subscribe-group-card">
                <div className="card-body">
                  <div className="subscribe-group-icon">
                    {group.icon}
                  </div>
                  <h5 className="subscribe-group-title">{group.name}</h5>
                  <p className="subscribe-group-description">{group.description}</p>
                  <button 
                    className="btn btn-primary subscribe-btn"
                    onClick={() => handleSubscribe(group.id, group.name)}
                  >
                    Subscribe
                  </button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info subscribe-no-results">
              No groups found matching "{searchQuery}"
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default User_Subscribe;
