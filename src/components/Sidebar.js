import React from 'react';
import { Link } from 'react-router-dom';
import './Sidebar.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const Sidebar = () => {
  return (
    <div className="sidebar-container">
      
      <div className="sidebar-brand">
        <h4 className="sidebar-brand-title">RW Tool</h4>
        <p className="sidebar-brand-subtitle">Bank Portal</p>
      </div>

      
      <div className="sidebar-nav-list">
        <div className="sidebar-nav-item">
          <Link to="/" className="sidebar-nav-link">
            <i className="bi bi-house-door me-2"></i>
            Dashboard
          </Link>
        </div>
        <div className="sidebar-nav-item">
          <Link to="/explore-groups" className="sidebar-nav-link">
            <i className="bi bi-search me-2"></i>
            Explore Groups
          </Link>
        </div>
        <div className="sidebar-nav-item">
          <Link to="/subscription-status" className="sidebar-nav-link">
            <i className="bi bi-clock-history me-2"></i>
            Subscription Status
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
