"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts"

export function EngagementMetrics() {
  const data = [
    { date: "May 7", retweets: 1200, likes: 2800, replies: 450 },
    { date: "May 8", retweets: 1800, likes: 4200, replies: 680 },
    { date: "May 9", retweets: 8500, likes: 15200, replies: 3200 }, // Peak engagement
    { date: "May 10", retweets: 6200, likes: 11800, replies: 2400 },
    { date: "May 11", retweets: 4800, likes: 9200, replies: 1800 },
    { date: "May 12", retweets: 3200, likes: 6800, replies: 1200 },
    { date: "May 13", retweets: 2400, likes: 5200, replies: 950 },
  ]

  return (
    <div className="h-[400px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip formatter={(value) => [value.toLocaleString(), ""]} />
          <Legend />
          <Line type="monotone" dataKey="retweets" stroke="#3b82f6" strokeWidth={2} activeDot={{ r: 6 }} />
          <Line type="monotone" dataKey="likes" stroke="#10b981" strokeWidth={2} activeDot={{ r: 6 }} />
          <Line type="monotone" dataKey="replies" stroke="#f59e0b" strokeWidth={2} activeDot={{ r: 6 }} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
