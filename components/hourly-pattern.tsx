"use client"

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts"

export function HourlyPattern() {
  // Data representing hourly sentiment on May 9th, 2023
  const data = [
    { hour: "6 AM", positive: 45, negative: 35, volume: 120 },
    { hour: "8 AM", positive: 42, negative: 38, volume: 280 },
    { hour: "10 AM", positive: 38, negative: 45, volume: 450 },
    { hour: "12 PM", positive: 25, negative: 65, volume: 890 }, // Arrest time
    { hour: "2 PM", positive: 15, negative: 75, volume: 1200 }, // Peak violence
    { hour: "4 PM", positive: 20, negative: 70, volume: 980 },
    { hour: "6 PM", positive: 28, negative: 62, volume: 750 },
    { hour: "8 PM", positive: 32, negative: 55, volume: 620 },
    { hour: "10 PM", positive: 35, negative: 50, volume: 480 },
  ]

  return (
    <div className="h-[300px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="hour" />
          <YAxis />
          <Tooltip formatter={(value, name) => [`${value}%`, name === "positive" ? "Positive" : "Negative"]} />
          <Bar dataKey="positive" fill="#22c55e" />
          <Bar dataKey="negative" fill="#ef4444" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}
