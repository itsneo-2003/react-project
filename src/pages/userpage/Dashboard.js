import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import './Dashboard.css';
import ReportSearch from '../../components/ReportSearch';  // Changed from '../components/ReportSearch'

const Dashboard = () => {
  // Mock data for subscribed groups (10 groups for demonstration)
  const subscribedGroups = [
    { id: 1, name: 'Credit Card Group', icon: '💳' },
    { id: 2, name: 'Risk Compliance Group', icon: '⚖️' },
    { id: 3, name: 'Loan Group', icon: '🏦' },
    { id: 4, name: 'Investment Group', icon: '📈' },
    { id: 5, name: 'Customer Service Group', icon: '👥' },
    { id: 6, name: 'Savings Account Group', icon: '💰' },
    { id: 7, name: 'Fraud Detection Group', icon: '🔒' },
    { id: 8, name: 'Digital Banking Group', icon: '📱' },
    { id: 9, name: 'Treasury Group', icon: '🏛️' },
    { id: 10, name: 'Operations Group', icon: '⚙️' },
  ];

  // Mock data for recently opened reports
  const recentReports = [
    { id: 1, reportName: 'Q4 Credit Card Analysis', groupName: 'Credit Card Group', dateAccessed: '2025-10-10' },
    { id: 2, reportName: 'Risk Assessment Report 2025', groupName: 'Risk Compliance Group', dateAccessed: '2025-10-09' },
    { id: 3, reportName: 'Loan Approval Metrics', groupName: 'Loan Group', dateAccessed: '2025-10-08' },
    { id: 4, reportName: 'Monthly Investment Summary', groupName: 'Investment Group', dateAccessed: '2025-10-07' },
    { id: 5, reportName: 'Customer Satisfaction Survey', groupName: 'Customer Service Group', dateAccessed: '2025-10-06' },
  ];

  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedReports, setSelectedReports] = useState([]);
  const groupsPerPage = 4;
  const totalPages = Math.ceil(subscribedGroups.length / groupsPerPage);

  // Get current groups to display
  const currentGroups = subscribedGroups.slice(
    currentIndex * groupsPerPage,
    (currentIndex + 1) * groupsPerPage
  );

  const handlePrevious = () => {
    setCurrentIndex((prev) => (prev > 0 ? prev - 1 : prev));
  };

  const handleNext = () => {
    setCurrentIndex((prev) => (prev < totalPages - 1 ? prev + 1 : prev));
  };

  // Handle individual checkbox selection
  const handleCheckboxChange = (reportId) => {
    if (selectedReports.includes(reportId)) {
      setSelectedReports(selectedReports.filter(id => id !== reportId));
    } else {
      setSelectedReports([...selectedReports, reportId]);
    }
  };

  // Handle select all checkbox
  const handleSelectAll = (e) => {
    if (e.target.checked) {
      const allReportIds = recentReports.map(report => report.id);
      setSelectedReports(allReportIds);
    } else {
      setSelectedReports([]);
    }
  };

  // Handle download selected reports
  const handleDownloadSelected = () => {
    if (selectedReports.length > 0) {
      console.log('Downloading reports with IDs:', selectedReports);
      alert(`Downloading ${selectedReports.length} report(s)`);
    }
  };

  // Handle bookmark/favourite
  const handleBookmark = (reportId, reportName) => {
    console.log('Bookmarking report:', reportId);
    alert(`Report "${reportName}" bookmarked!`);
  };

  // Handle individual report download
  const handleIndividualDownload = (reportId, reportName) => {
    console.log('Downloading report:', reportId);
    alert(`Downloading report: "${reportName}"`);
  };

  return (
    <div className="dashboard-container">
      {/* Header with Title and Search */}
      <div className="dashboard-header">
        <div className="dashboard-header-left">
          <h3 className="groups-title">My Subscribed Groups</h3>
        </div>
        <div className="dashboard-header-right">
          <ReportSearch />
        </div>
      </div>

      {/* Subscribed Groups Section */}
      <div className="groups-section">
        <div className="groups-carousel">
          {/* Previous Button */}
          <button
            className="btn carousel-btn carousel-btn-prev"
            onClick={handlePrevious}
            disabled={currentIndex === 0}
          >
            &#8249;
          </button>

          {/* Groups Container */}
          <div className="groups-grid-container">
            <div className="row g-3">
              {currentGroups.map((group) => (
                <div key={group.id} className="col-md-6 col-lg-3">
                  <div className="card shadow-sm group-card">
                    <div className="card-body text-center">
                      <h5 className="card-title group-card-title">{group.name}</h5>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Next Button */}
          <button
            className="btn carousel-btn carousel-btn-next"
            onClick={handleNext}
            disabled={currentIndex === totalPages - 1}
          >
            &#8250;
          </button>
        </div>
        
        {/* Page Indicator */}
        <div className="page-indicator">
          <small className="text-muted">
            Page {currentIndex + 1} of {totalPages}
          </small>
        </div>
      </div>

      {/* Recently Opened Reports Section */}
      <div className="reports-section">
        <div className="reports-header">
          <h3 className="reports-title">Recently Opened Reports</h3>
          <button 
            className="btn download-btn"
            onClick={handleDownloadSelected}
            disabled={selectedReports.length === 0}
          >
            Download Selected ({selectedReports.length})
          </button>
        </div>
        <div className="table-responsive">
          <table className="table table-hover table-striped">
            <thead className="table-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Report Name</th>
                <th scope="col">Group</th>
                <th scope="col">Date Accessed</th>
                <th scope="col" style={{ width: '80px', textAlign: 'center' }}>
                  <i className="bi bi-star-fill"></i>
                </th>
                <th scope="col" style={{ width: '80px', textAlign: 'center' }}>
                  <i className="bi bi-download"></i>
                </th>
                <th scope="col" style={{ width: '80px', textAlign: 'center' }}>
                  <input 
                    type="checkbox" 
                    className="form-check-input table-checkbox"
                    onChange={handleSelectAll}
                    checked={selectedReports.length === recentReports.length && recentReports.length > 0}
                  />
                </th>
              </tr>
            </thead>
            <tbody>
              {recentReports.map((report, index) => (
                <tr key={report.id} className="reports-table">
                  <th scope="row">{index + 1}</th>
                  <td>{report.reportName}</td>
                  <td>{report.groupName}</td>
                  <td>{report.dateAccessed}</td>
                  <td style={{ textAlign: 'center' }}>
                    <i 
                      className="bi bi-star action-icon star-icon"
                      onClick={() => handleBookmark(report.id, report.reportName)}
                    ></i>
                  </td>
                  <td style={{ textAlign: 'center' }}>
                    <i 
                      className="bi bi-download action-icon download-icon"
                      onClick={() => handleIndividualDownload(report.id, report.reportName)}
                    ></i>
                  </td>
                  <td style={{ textAlign: 'center' }}>
                    <input 
                      type="checkbox"
                      className="form-check-input table-checkbox"
                      checked={selectedReports.includes(report.id)}
                      onChange={() => handleCheckboxChange(report.id)}
                    />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;