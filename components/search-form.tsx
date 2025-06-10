"use client"

import type React from "react"

import { useState } from "react"
import { Search, Calendar, Hash } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

interface SearchFormProps {
  defaultQuery?: string
}

export function SearchForm({ defaultQuery = "" }: SearchFormProps) {
  const [query, setQuery] = useState(defaultQuery)
  const [dateRange, setDateRange] = useState("2023-05-07 to 2023-05-15")
  const [isLoading, setIsLoading] = useState(false)

  // Popular keywords from 9th May 2023 incident (English and Urdu)
  const popularKeywords = [
    "#ImranKhan",
    "#9thMay",
    "#عمران_خان",
    "#نو_مئی",
    "#Violence",
    "#تشدد",
    "#PTI",
    "#پی_ٹی_آئی",
    "#Arrest",
    "#گرفتاری",
    "#Pakistan",
    "#پاکستان",
    "#Justice",
    "#انصاف",
    "#Lahore",
    "#لاہور",
    "#Islamabad",
    "#اسلام_آباد",
    "#Protests",
    "#احتجاج",
  ]

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!query.trim()) return

    setIsLoading(true)
    // In a real app, this would trigger the Twitter data collection
    // and sentiment analysis process
    setTimeout(() => {
      setIsLoading(false)
    }, 1500)
  }

  const addKeyword = (keyword: string) => {
    const currentQuery = query.trim()
    if (currentQuery && !currentQuery.includes(keyword)) {
      setQuery(currentQuery + " OR " + keyword)
    } else if (!currentQuery) {
      setQuery(keyword)
    }
  }

  const clearQuery = () => {
    setQuery("")
  }

  return (
    <Card>
      <CardContent className="pt-6 space-y-4">
        {/* Main Search Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="flex w-full items-center space-x-2">
            <div className="relative flex-1">
              <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
              <Input
                type="text"
                placeholder="Enter search terms: #ImranKhan OR #عمران_خان OR #9thMay OR #نو_مئی"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                className="pl-8 text-sm"
              />
            </div>
            <Button type="submit" disabled={isLoading} className="px-6">
              {isLoading ? "Analyzing..." : "Track Sentiment"}
            </Button>
          </div>

          {/* Date Range */}
          <div className="flex items-center space-x-2">
            <Calendar className="h-4 w-4 text-muted-foreground" />
            <Input
              type="text"
              placeholder="Date range"
              value={dateRange}
              onChange={(e) => setDateRange(e.target.value)}
              className="w-64 text-sm"
            />
            <Button type="button" variant="outline" size="sm" onClick={clearQuery}>
              Clear
            </Button>
          </div>
        </form>

        {/* Popular Keywords */}
        <div className="space-y-3">
          <div className="flex items-center space-x-2">
            <Hash className="h-4 w-4 text-muted-foreground" />
            <span className="text-sm font-medium text-gray-700">Popular Keywords (May 9, 2023):</span>
          </div>

          <div className="flex flex-wrap gap-2">
            {popularKeywords.map((keyword, index) => (
              <Badge
                key={index}
                variant="secondary"
                className="cursor-pointer hover:bg-blue-100 hover:text-blue-800 transition-colors"
                onClick={() => addKeyword(keyword)}
              >
                {keyword}
              </Badge>
            ))}
          </div>
        </div>

        {/* Search Tips */}
        <div className="text-xs text-gray-500 bg-gray-50 p-3 rounded-md">
          <strong>Search Tips:</strong> Use OR between terms • Add # for hashtags • Mix English/Urdu: #ImranKhan OR
          #عمران_خان • Date format: YYYY-MM-DD to YYYY-MM-DD
        </div>
      </CardContent>
    </Card>
  )
}
