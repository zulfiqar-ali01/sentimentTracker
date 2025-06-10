"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { TrendingUp, TrendingDown, MessageSquare, Users, BarChart2, AlertTriangle } from "lucide-react"

export function SentimentOverview() {
  // In a real app, this data would come from the Twitter API and sentiment analysis
  const sentimentData = {
    overall: 42, // Lower sentiment due to the violent incident
    totalMentions: 89750, // Higher volume due to major incident
    positivePercentage: 42,
    negativePercentage: 45,
    neutralPercentage: 13,
    engagement: 156780,
    reachInMillions: 8.9, // Higher reach due to international attention
    trending: "down", // Negative trend due to violence
  }

  return (
    <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
      {/* Overall Sentiment Card */}
      <Card className="relative overflow-hidden border-0 bg-gradient-to-br from-orange-50 to-red-50 shadow-lg">
        <div className="absolute inset-0 bg-gradient-to-br from-orange-500/10 to-red-500/10" />
        <CardHeader className="relative flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium text-gray-700">Overall Sentiment</CardTitle>
          <div className="flex items-center space-x-1">
            {sentimentData.trending === "up" ? (
              <TrendingUp className="h-5 w-5 text-green-600" />
            ) : (
              <TrendingDown className="h-5 w-5 text-red-600" />
            )}
            <AlertTriangle className="h-4 w-4 text-orange-500" />
          </div>
        </CardHeader>
        <CardContent className="relative">
          <div className="text-3xl font-bold text-gray-900">{sentimentData.overall}%</div>
          <div className="mt-3 space-y-2">
            <div className="flex items-center justify-between text-xs">
              <span className="text-gray-600">Sentiment Distribution</span>
            </div>
            <div className="h-2 w-full rounded-full bg-gray-200">
              <div
                className="h-2 rounded-full bg-gradient-to-r from-red-500 via-yellow-500 to-green-500"
                style={{ width: `${sentimentData.overall}%` }}
              />
            </div>
            <div className="flex justify-between text-xs text-gray-600">
              <span className="flex items-center">
                <div className="mr-1 h-2 w-2 rounded-full bg-green-500"></div>
                {sentimentData.positivePercentage}%
              </span>
              <span className="flex items-center">
                <div className="mr-1 h-2 w-2 rounded-full bg-red-500"></div>
                {sentimentData.negativePercentage}%
              </span>
              <span className="flex items-center">
                <div className="mr-1 h-2 w-2 rounded-full bg-gray-400"></div>
                {sentimentData.neutralPercentage}%
              </span>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Total Mentions Card */}
      <Card className="relative overflow-hidden border-0 bg-gradient-to-br from-blue-50 to-indigo-50 shadow-lg">
        <div className="absolute inset-0 bg-gradient-to-br from-blue-500/10 to-indigo-500/10" />
        <div className="absolute right-4 top-4 opacity-20">
          <MessageSquare className="h-12 w-12 text-blue-500" />
        </div>
        <CardHeader className="relative flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium text-gray-700">Total Mentions</CardTitle>
          <MessageSquare className="h-5 w-5 text-blue-600" />
        </CardHeader>
        <CardContent className="relative">
          <div className="text-3xl font-bold text-gray-900">{sentimentData.totalMentions.toLocaleString()}</div>
          <div className="mt-2 flex items-center space-x-2">
            <div className="flex items-center text-sm text-green-600">
              <TrendingUp className="mr-1 h-3 w-3" />+{Math.floor(Math.random() * 20) + 15}%
            </div>
            <span className="text-xs text-gray-500">vs last period</span>
          </div>
          <div className="mt-3 h-1 w-full rounded-full bg-blue-200">
            <div className="h-1 w-3/4 rounded-full bg-gradient-to-r from-blue-400 to-blue-600"></div>
          </div>
        </CardContent>
      </Card>

      {/* Engagement Card */}
      <Card className="relative overflow-hidden border-0 bg-gradient-to-br from-green-50 to-emerald-50 shadow-lg">
        <div className="absolute inset-0 bg-gradient-to-br from-green-500/10 to-emerald-500/10" />
        <div className="absolute right-4 top-4 opacity-20">
          <Users className="h-12 w-12 text-green-500" />
        </div>
        <CardHeader className="relative flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium text-gray-700">Total Engagement</CardTitle>
          <Users className="h-5 w-5 text-green-600" />
        </CardHeader>
        <CardContent className="relative">
          <div className="text-3xl font-bold text-gray-900">{sentimentData.engagement.toLocaleString()}</div>
          <div className="mt-2 text-xs text-gray-600">Likes, retweets, and replies</div>
          <div className="mt-3 grid grid-cols-3 gap-2 text-xs">
            <div className="text-center">
              <div className="font-semibold text-blue-600">45.2K</div>
              <div className="text-gray-500">Retweets</div>
            </div>
            <div className="text-center">
              <div className="font-semibold text-red-600">78.5K</div>
              <div className="text-gray-500">Likes</div>
            </div>
            <div className="text-center">
              <div className="font-semibold text-yellow-600">33.1K</div>
              <div className="text-gray-500">Replies</div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Potential Reach Card */}
      <Card className="relative overflow-hidden border-0 bg-gradient-to-br from-purple-50 to-pink-50 shadow-lg">
        <div className="absolute inset-0 bg-gradient-to-br from-purple-500/10 to-pink-500/10" />
        <div className="absolute right-4 top-4 opacity-20">
          <BarChart2 className="h-12 w-12 text-purple-500" />
        </div>
        <CardHeader className="relative flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium text-gray-700">Potential Reach</CardTitle>
          <BarChart2 className="h-5 w-5 text-purple-600" />
        </CardHeader>
        <CardContent className="relative">
          <div className="text-3xl font-bold text-gray-900">{sentimentData.reachInMillions}M</div>
          <div className="mt-2 text-xs text-gray-600">Estimated audience size</div>
          <div className="mt-3 space-y-2">
            <div className="flex justify-between text-xs">
              <span className="text-gray-600">Coverage</span>
              <span className="font-medium text-purple-600">89%</span>
            </div>
            <div className="h-1 w-full rounded-full bg-purple-200">
              <div className="h-1 w-[89%] rounded-full bg-gradient-to-r from-purple-400 to-pink-500"></div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
