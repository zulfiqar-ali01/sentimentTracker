"use client"

import { AlertTriangle, TrendingDown, Users, Clock, Shield, Activity } from "lucide-react"

export function KeyMetrics() {
  const metrics = [
    {
      label: "Peak Violence Hour",
      value: "2:00 PM",
      icon: AlertTriangle,
      color: "text-red-500",
      bgColor: "bg-red-50",
      borderColor: "border-red-200",
      change: "Critical",
      changeColor: "text-red-600",
    },
    {
      label: "Sentiment Drop",
      value: "-38%",
      icon: TrendingDown,
      color: "text-red-500",
      bgColor: "bg-red-50",
      borderColor: "border-red-200",
      change: "Severe",
      changeColor: "text-red-600",
    },
    {
      label: "Active Users",
      value: "45.2K",
      icon: Users,
      color: "text-blue-500",
      bgColor: "bg-blue-50",
      borderColor: "border-blue-200",
      change: "+285%",
      changeColor: "text-blue-600",
    },
    {
      label: "Crisis Duration",
      value: "8 hours",
      icon: Clock,
      color: "text-orange-500",
      bgColor: "bg-orange-50",
      borderColor: "border-orange-200",
      change: "Extended",
      changeColor: "text-orange-600",
    },
    {
      label: "Safety Alerts",
      value: "127",
      icon: Shield,
      color: "text-purple-500",
      bgColor: "bg-purple-50",
      borderColor: "border-purple-200",
      change: "High",
      changeColor: "text-purple-600",
    },
    {
      label: "Peak Activity",
      value: "1.2K/min",
      icon: Activity,
      color: "text-green-500",
      bgColor: "bg-green-50",
      borderColor: "border-green-200",
      change: "Record",
      changeColor: "text-green-600",
    },
  ]

  return (
    <div className="space-y-3">
      {metrics.map((metric, index) => (
        <div
          key={index}
          className={`flex items-center justify-between p-3 rounded-lg border ${metric.bgColor} ${metric.borderColor} transition-all hover:shadow-md`}
        >
          <div className="flex items-center space-x-3">
            <div className={`p-2 rounded-full ${metric.bgColor} border ${metric.borderColor}`}>
              <metric.icon className={`h-4 w-4 ${metric.color}`} />
            </div>
            <div>
              <span className="text-sm font-medium text-gray-700">{metric.label}</span>
              <div className={`text-xs ${metric.changeColor} font-medium`}>{metric.change}</div>
            </div>
          </div>
          <div className="text-right">
            <span className="text-lg font-bold text-gray-900">{metric.value}</span>
          </div>
        </div>
      ))}
    </div>
  )
}
