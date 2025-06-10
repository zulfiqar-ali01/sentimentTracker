"use client"

import { Badge } from "@/components/ui/badge"
import { Hash, TrendingUp } from "lucide-react"

export function TopHashtags() {
  const hashtags = [
    { tag: "#9thMay", urdu: "#نو_مئی", count: "15.2K", sentiment: "negative", trend: "+520%" },
    { tag: "#ImranKhan", urdu: "#عمران_خان", count: "12.8K", sentiment: "positive", trend: "+180%" },
    { tag: "#عمران_خان", count: "11.5K", sentiment: "positive", trend: "+165%" },
    { tag: "#Violence", urdu: "#تشدد", count: "8.9K", sentiment: "negative", trend: "+450%" },
    { tag: "#PTI", urdu: "#پی_ٹی_آئی", count: "7.6K", sentiment: "positive", trend: "+125%" },
    { tag: "#Justice", urdu: "#انصاف", count: "5.2K", sentiment: "positive", trend: "+89%" },
    { tag: "#Pakistan", urdu: "#پاکستان", count: "4.8K", sentiment: "neutral", trend: "+67%" },
    { tag: "#Arrest", urdu: "#گرفتاری", count: "4.1K", sentiment: "negative", trend: "+234%" },
    { tag: "#لاہور", count: "3.8K", sentiment: "neutral", trend: "+189%" },
    { tag: "#احتجاج", count: "3.2K", sentiment: "neutral", trend: "+156%" },
  ]

  const getSentimentStyle = (sentiment: string) => {
    switch (sentiment) {
      case "positive":
        return {
          badge: "bg-green-100 text-green-800 hover:bg-green-200 border-green-200",
          bg: "bg-green-50",
          border: "border-green-200",
        }
      case "negative":
        return {
          badge: "bg-red-100 text-red-800 hover:bg-red-200 border-red-200",
          bg: "bg-red-50",
          border: "border-red-200",
        }
      default:
        return {
          badge: "bg-gray-100 text-gray-800 hover:bg-gray-200 border-gray-200",
          bg: "bg-gray-50",
          border: "border-gray-200",
        }
    }
  }

  return (
    <div className="space-y-3">
      {hashtags.slice(0, 8).map((hashtag, index) => {
        const style = getSentimentStyle(hashtag.sentiment)
        return (
          <div
            key={index}
            className={`flex items-center justify-between p-3 rounded-lg border ${style.bg} ${style.border} transition-all hover:shadow-md`}
          >
            <div className="flex items-center space-x-3">
              <div className={`p-2 rounded-full ${style.bg} border ${style.border}`}>
                <Hash className="h-3 w-3 text-gray-600" />
              </div>
              <div>
                <Badge variant="secondary" className={`${style.badge} border font-medium mb-1`}>
                  {hashtag.tag}
                </Badge>
                {hashtag.urdu && <div className="text-xs text-gray-600 mt-1">{hashtag.urdu}</div>}
                <div className="flex items-center mt-1 space-x-1">
                  <TrendingUp className="h-3 w-3 text-green-500" />
                  <span className="text-xs text-green-600 font-medium">{hashtag.trend}</span>
                </div>
              </div>
            </div>
            <div className="text-right">
              <div className="text-lg font-bold text-gray-900">{hashtag.count}</div>
              <div className="text-xs text-gray-500">mentions</div>
            </div>
          </div>
        )
      })}
    </div>
  )
}
