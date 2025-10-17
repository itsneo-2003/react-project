import React, { useState } from 'react';
import './Subscription_Status.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const Subscription_Status = () => {
  
  const [subscriptionRequests] = useState([
    { id: 1, groupName: 'Credit Card Group', dateRequested: '2025-10-01', status: 'approved' },
    { id: 2, groupName: 'Risk Compliance Group', dateRequested: '2025-10-05', status: 'pending' },
    { id: 3, groupName: 'Loan Group', dateRequested: '2025-10-08', status: 'rejected' },
    { id: 4, groupName: 'Investment Group', dateRequested: '2025-10-10', status: 'approved' },
    { id: 5, groupName: 'Digital Banking Group', dateRequested: '2025-10-12', status: 'pending' },
    { id: 6, groupName: 'Treasury Group', dateRequested: '2025-10-13', status: 'pending' },
    { id: 7, groupName: 'Operations Group', dateRequested: '2025-10-14', status: 'rejected' },
    { id: 8, groupName: 'Fraud Detection Group', dateRequested: '2025-10-15', status: 'approved' },
  ]);

  const [activeFilter, setActiveFilter] = useState('all');

  
  const filteredRequests = activeFilter === 'all' 
    ? subscriptionRequests 
    : subscriptionRequests.filter(request => request.status === activeFilter);


  const getStatusClass = (status) => {
    switch(status) {
      case 'pending': return 'status-pending';
      case 'approved': return 'status-approved';
      case 'rejected': return 'status-rejected';
      default: return '';
    }
  };

  
  const capitalizeStatus = (status) => {
    return status.charAt(0).toUpperCase() + status.slice(1);
  };

  return (
    <div className="subscription-status-container">
      <div className="subscription-status-header">
        <h3 className="subscription-status-title">Subscription Status</h3>
        <p className="subscription-status-subtitle">Track your group subscription requests</p>
      </div>

      <div className="subscription-summary">
        <div className="summary-item">
          <span className="summary-label">Total Requests:</span>
          <span className="summary-value">{subscriptionRequests.length}</span>
        </div>
        <div className="summary-item">
          <span className="summary-label">Pending:</span>
          <span className="summary-value">
            {subscriptionRequests.filter(r => r.status === 'pending').length}
          </span>
        </div>
        <div className="summary-item">
          <span className="summary-label">Approved:</span>
          <span className="summary-value">
            {subscriptionRequests.filter(r => r.status === 'approved').length}
          </span>
        </div>
        <div className="summary-item">
          <span className="summary-label">Rejected:</span>
          <span className="summary-value">
            {subscriptionRequests.filter(r => r.status === 'rejected').length}
          </span>
        </div>
      </div>
      <br></br>

      
      <div className="filter-buttons-container">
        <button 
          className={`filter-btn filter-all ${activeFilter === 'all' ? 'active' : ''}`}
          onClick={() => setActiveFilter('all')}
        >
          All
        </button>
        <button 
          className={`filter-btn filter-pending ${activeFilter === 'pending' ? 'active' : ''}`}
          onClick={() => setActiveFilter('pending')}
        >
          Pending
        </button>
        <button 
          className={`filter-btn filter-approved ${activeFilter === 'approved' ? 'active' : ''}`}
          onClick={() => setActiveFilter('approved')}
        >
          Approved
        </button>
        <button 
          className={`filter-btn filter-rejected ${activeFilter === 'rejected' ? 'active' : ''}`}
          onClick={() => setActiveFilter('rejected')}
        >
          Rejected
        </button>
      </div>
      <br></br>

      <div className="table-wrapper">
        <table className="table table-hover subscription-table">
          <thead className="table-dark">
            <tr>
              <th scope="col">#</th>
              <th scope="col">Group Name</th>
              <th scope="col">Date Requested</th>
              <th scope="col">Status</th>
            </tr>
          </thead>
          <tbody>
            {filteredRequests.length > 0 ? (
              filteredRequests.map((request, index) => (
                <tr key={request.id}>
                  <th scope="row">{index + 1}</th>
                  <td>{request.groupName}</td>
                  <td>{request.dateRequested}</td>
                  <td>
                    <span className={`status-badge ${getStatusClass(request.status)}`}>
                      {capitalizeStatus(request.status)}
                    </span>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4" className="text-center text-muted">
                  No subscription requests found
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

    
      
    </div>
  );
};

export default Subscription_Status;
