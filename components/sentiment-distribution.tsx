"use client"

import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from "recharts"

export function SentimentDistribution() {
  const data = [
    { name: "Positive", value: 42, color: "#22c55e" },
    { name: "Negative", value: 45, color: "#ef4444" },
    { name: "Neutral", value: 13, color: "#94a3b8" },
  ]

  return (
    <div className="h-[200px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie data={data} cx="50%" cy="50%" innerRadius={40} outerRadius={80} paddingAngle={5} dataKey="value">
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={entry.color} />
            ))}
          </Pie>
          <Tooltip formatter={(value) => [`${value}%`, "Percentage"]} />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  )
}
