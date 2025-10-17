import React, { useState } from "react";
import reportsData from "../data/reports.json";
import 'bootstrap/dist/css/bootstrap.min.css';
import './ReportSearch.css';

function ReportSearch() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = (searchText) => {
    const trimmed = searchText.trim();
    if (trimmed === "") {
      setResults([]);
      return;
    }

    const filtered = reportsData.filter((report) =>
      report.reportName.toLowerCase().includes(trimmed.toLowerCase())
    );
    setResults(filtered);
  };

  const handleInputChange = (e) => {
    const value = e.target.value;
    setQuery(value);
    handleSearch(value);
  };

  return (
    <div className="report-search-container">
      <div className="search-bar-wrapper">
        <div className="search-input-group">
          <input
            type="text"
            className="form-control search-input"
            value={query}
            onChange={handleInputChange}
            placeholder="Enter report name..."
          />
          <button
            className="btn btn-primary search-button"
            onClick={() => handleSearch(query)}
          >
            Search
          </button>
        </div>
      </div>

      
      <div className="search-results-wrapper">
        {results.length > 0 ? (
          <table className="table table-bordered search-results-table">
            <thead className="table-light">
              <tr>
                <th>Report Name</th>
                <th>Group</th>
                <th>Upload Date</th>
              </tr>
            </thead>
            <tbody>
              {results.map((r, i) => (
                <tr key={i}>
                  <td>{r.reportName}</td>
                  <td>{r.reportGroup}</td>
                  <td>{r.uploadDate}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          query && <p className="no-results-message">No reports found.</p>
        )}
      </div>
    </div>
  );
}

export default ReportSearch;
