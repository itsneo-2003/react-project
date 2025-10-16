import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/userpage/Dashboard';
import User_Subscribe from './pages/userpage/User_Subscribe';
import Subscription_Status from './pages/userpage/Subscription_Status';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Router>
      <div>
        <Sidebar />
        <div style={{ marginLeft: '250px' }}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/explore-groups" element={<User_Subscribe />} />
            <Route path="/subscription-status" element={<Subscription_Status />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;