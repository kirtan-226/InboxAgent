import React from "react";

function EmailCard({ subject, from, body }) {
  return (
    <div className="bg-white shadow rounded-lg p-4 border border-gray-200">
      <h2 className="text-lg font-semibold text-gray-800">{subject}</h2>
      <p className="text-sm text-gray-500">From: {from}</p>
      <p className="mt-2 text-gray-700">{body}</p>
    </div>
  );
}

export default EmailCard;
