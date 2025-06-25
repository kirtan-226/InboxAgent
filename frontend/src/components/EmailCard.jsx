
import React from "react";

function EmailCard({ subject, from, body }) {
  return (
    <div className="bg-white shadow-md p-4 rounded-lg border border-gray-200">
      <h2 className="text-xl font-semibold text-gray-800">{subject}</h2>
      <p className="text-sm text-gray-500">From: {from}</p>
      <p className="text-gray-700 mt-2">{body}</p>
    </div>
  );
}

export default EmailCard;
