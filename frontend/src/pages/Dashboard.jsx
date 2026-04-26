import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../api";

function Dashboard() {
  const [drafts, setDrafts] = useState([]);
  const [selectedDraft, setSelectedDraft] = useState(null);
  const [filter, setFilter] = useState("all");
  const navigate = useNavigate();

  useEffect(() => {
    // Basic auth check
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/");
      return;
    }

    const fetchDrafts = () => {
      API.get("/api/drafts")
        .then(res => {
          if (Array.isArray(res.data)) {
            setDrafts(res.data);
          }
        })
        .catch(err => console.error("Error fetching drafts:", err));
    };

    fetchDrafts(); // initial load
    const interval = setInterval(fetchDrafts, 5000); // every 5 sec
    return () => clearInterval(interval); // cleanup
  }, [navigate]);

  // ✅ APPROVE
  const handleApprove = () => {
    API.post(`/api/draft/${selectedDraft.id}/approve`)
      .then(() => {
        const updated = { ...selectedDraft, status: "approved" };
        setSelectedDraft(updated);

        setDrafts(drafts.map(d =>
          d.id === selectedDraft.id ? updated : d
        ));
      })
      .catch(err => console.error("Error approving:", err));
  };

  // ❌ REJECT
  const handleReject = () => {
    API.post(`/api/draft/${selectedDraft.id}/reject`)
      .then(() => {
        const updated = { ...selectedDraft, status: "rejected" };
        setSelectedDraft(updated);

        setDrafts(drafts.map(d =>
          d.id === selectedDraft.id ? updated : d
        ));
      })
      .catch(err => console.error("Error rejecting:", err));
  };

  // ✅ FILTER LOGIC
  const filteredDrafts = drafts.filter(d => {
    if (filter === "all") return true;
    return d.status === filter;
  });

  const getStatusClass = (status) => {
    if (status === "approved") return "status-approved";
    if (status === "rejected") return "status-rejected";
    if (status === "pending") return "status-pending";
    return "";
  };

  return (
    <div className="dashboard-container">
      
      {/* LEFT SIDE: SIDEBAR */}
      <div className="dashboard-sidebar">
        <div>
          <h2>Draft List</h2>
          <p style={{ fontSize: '0.9rem', marginBottom: '16px' }}>Manage and review AI generated drafts</p>
          
          {/* ✅ FILTER BUTTONS */}
          <div className="filter-group">
            <button 
              className={`filter-btn ${filter === "all" ? "active" : ""}`} 
              onClick={() => setFilter("all")}
            >
              All
            </button>
            <button 
              className={`filter-btn ${filter === "pending" ? "active" : ""}`} 
              onClick={() => setFilter("pending")}
            >
              Pending
            </button>
            <button 
              className={`filter-btn ${filter === "approved" ? "active" : ""}`} 
              onClick={() => setFilter("approved")}
            >
              Approved
            </button>
            <button 
              className={`filter-btn ${filter === "rejected" ? "active" : ""}`} 
              onClick={() => setFilter("rejected")}
            >
              Rejected
            </button>
          </div>
        </div>

        {/* ✅ USE FILTERED DATA */}
        <div className="draft-list">
          {filteredDrafts.length === 0 ? (
            <p style={{ textAlign: "center", marginTop: "20px" }}>No drafts found.</p>
          ) : (
            filteredDrafts.map((draft) => (
              <div
                key={draft.id}
                className={`draft-item ${selectedDraft?.id === draft.id ? 'active' : ''}`}
                onClick={() => setSelectedDraft(draft)}
              >
                <div className="draft-item-header">
                  <h4 style={{ margin: 0, fontSize: "1.05rem" }}>ID: {draft.id}</h4>
                  <span className={`status-pill ${getStatusClass(draft.status)}`}>
                    {draft.status}
                  </span>
                </div>
                <div className="draft-item-preview">
                  {draft.reply}
                </div>
              </div>
            ))
          )}
        </div>
      </div>

      {/* RIGHT SIDE: MAIN CONTENT */}
      <div className="dashboard-main">
        {!selectedDraft ? (
          <div style={{ display: 'flex', height: '100%', alignItems: 'center', justifyContent: 'center' }}>
            <p style={{ fontSize: '1.2rem', color: 'var(--text-muted)' }}>Select a draft from the sidebar to view details</p>
          </div>
        ) : (
          <div className="draft-detail-card">
            <div className="draft-detail-header">
              <div>
                <h2>Draft #{selectedDraft.id}</h2>
                <p>Event ID: {selectedDraft.event_id}</p>
              </div>
              <span className={`status-pill ${getStatusClass(selectedDraft.status)}`} style={{ fontSize: '0.9rem', padding: '6px 16px' }}>
                {selectedDraft.status}
              </span>
            </div>

            <div className="draft-reply-content">
              {selectedDraft.reply}
            </div>

            {/* ACTION BUTTONS */}
            <div className="action-buttons">
              <button className="btn btn-success" onClick={handleApprove}>
                <svg width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginRight: '8px' }}>
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                Approve
              </button>

              <button className="btn btn-danger" onClick={handleReject}>
                <svg width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginRight: '8px' }}>
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
                Reject
              </button>
            </div>
          </div>
        )}
      </div>

    </div>
  );
}

export default Dashboard;