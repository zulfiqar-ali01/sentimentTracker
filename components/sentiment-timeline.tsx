"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts"

export function SentimentTimeline() {
  // Update the data array to reflect the May 9th incident timeline
  const data = [
    { date: "May 7", positive: 55, negative: 30, neutral: 15 },
    { date: "May 8", positive: 48, negative: 35, neutral: 17 },
    { date: "May 9", positive: 25, negative: 65, neutral: 10 }, // Day of incident
    { date: "May 10", positive: 30, negative: 58, neutral: 12 },
    { date: "May 11", positive: 35, negative: 52, neutral: 13 },
    { date: "May 12", positive: 40, negative: 48, neutral: 12 },
    { date: "May 13", positive: 42, negative: 45, neutral: 13 },
  ]

  return (
    <div className="space-y-4">
      <div className="h-[300px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="positive" stroke="#22c55e" strokeWidth={2} activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="negative" stroke="#ef4444" strokeWidth={2} />
            <Line type="monotone" dataKey="neutral" stroke="#94a3b8" strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}
