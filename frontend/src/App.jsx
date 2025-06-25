import React, { useEffect, useState } from "react";
import axios from "axios";
import EmailCard from "./components/EmailCard";

function App() {
  const [emails, setEmails] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/emails/")
      .then((res) => setEmails(res.data.emails || []))
      .catch((err) => console.error("Error fetching emails:", err));
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6 text-center text-blue-700">📬 Your Inbox</h1>
      <div className="space-y-4">
        {emails.length > 0 ? (
          emails.map((email, index) => (
            <EmailCard key={index} subject={email.subject} from={email.from} body={email.body} />
          ))
        ) : (
          <p className="text-center text-gray-500">No emails found.</p>
        )}
      </div>
    </div>
  );
}

export default App;
