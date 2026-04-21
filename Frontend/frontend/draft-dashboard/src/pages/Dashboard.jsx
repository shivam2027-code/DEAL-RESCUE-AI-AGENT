import { useEffect, useState } from "react";

function Dashboard() {
  const [drafts, setDrafts] = useState([]);
  const [selectedDraft, setSelectedDraft] = useState(null);
  const [filter, setFilter] = useState("all"); // ✅ filter state

  useEffect(() => {
  const fetchDrafts = () => {
    fetch("http://localhost:8000/api/drafts")
      .then(res => res.json())
      .then(data => {
        setDrafts(data);
      });
  };

  fetchDrafts(); // initial load

  const interval = setInterval(fetchDrafts, 5000); // every 5 sec

  return () => clearInterval(interval); // cleanup
}, []);





  // ✅ APPROVE
  const handleApprove = () => {
    fetch(`http://localhost:8000/api/draft/${selectedDraft.id}/approve`, {
      method: "POST",
    })
      .then(res => res.json())
      .then(() => {
        const updated = { ...selectedDraft, status: "approved" };
        setSelectedDraft(updated);

        setDrafts(drafts.map(d =>
          d.id === selectedDraft.id ? updated : d
        ));
      });
  };

  // ❌ REJECT
  const handleReject = () => {
    fetch(`http://localhost:8000/api/draft/${selectedDraft.id}/reject`, {
      method: "POST",
    })
      .then(res => res.json())
      .then(() => {
        const updated = { ...selectedDraft, status: "rejected" };
        setSelectedDraft(updated);

        setDrafts(drafts.map(d =>
          d.id === selectedDraft.id ? updated : d
        ));
      });
  };

  // ✅ FILTER LOGIC
  const filteredDrafts = drafts.filter(d => {
    if (filter === "all") return true;
    return d.status === filter;
  });

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      
      {/* LEFT SIDE */}
      <div style={{ width: "40%", borderRight: "1px solid gray", padding: "10px" }}>
        <h2>Draft List</h2>

        {/* ✅ FILTER BUTTONS */}
        <div style={{ marginBottom: "10px" }}>
          <button onClick={() => setFilter("all")}>All</button>
          <button onClick={() => setFilter("pending")} style={{ marginLeft: "5px" }}>Pending</button>
          <button onClick={() => setFilter("approved")} style={{ marginLeft: "5px" }}>Approved</button>
          <button onClick={() => setFilter("rejected")} style={{ marginLeft: "5px" }}>Rejected</button>
        </div>

        {/* ✅ USE FILTERED DATA */}
        {filteredDrafts.map((draft) => (
          <div
            key={draft.id}
            onClick={() => setSelectedDraft(draft)}
            style={{
              padding: "10px",
              marginBottom: "10px",
              border: "1px solid gray",
              cursor: "pointer",
              background: selectedDraft?.id === draft.id ? "#222" : "transparent"
            }}
          >
            <p><b>ID:</b> {draft.id}</p>
            <p><b>Status:</b> {draft.status}</p>
            <p>{draft.reply.slice(0, 80)}...</p>
          </div>
        ))}
      </div>

      {/* RIGHT SIDE */}
      <div style={{ width: "60%", padding: "20px" }}>
        <h2>Draft Detail</h2>

        {!selectedDraft ? (
          <p>Select a draft to view details</p>
        ) : (
          <div>
            <p><b>ID:</b> {selectedDraft.id}</p>
            <p><b>Status:</b> {selectedDraft.status}</p>
            <p><b>Event ID:</b> {selectedDraft.event_id}</p>

            <hr />

            <p>{selectedDraft.reply}</p>

            {/* ACTION BUTTONS */}
            <div style={{ marginTop: "20px" }}>
              <button onClick={handleApprove} style={{ marginRight: "10px" }}>
                Approve
              </button>

              <button onClick={handleReject}>
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