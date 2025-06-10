import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { SentimentOverview } from "@/components/sentiment-overview"
import { SentimentTimeline } from "@/components/sentiment-timeline"
import { SentimentWordcloud } from "@/components/sentiment-wordcloud"
import { RegionMap } from "@/components/region-map"
import { SearchForm } from "@/components/search-form"
import { SentimentDistribution } from "@/components/sentiment-distribution"
import { EngagementMetrics } from "@/components/engagement-metrics"
import { HourlyPattern } from "@/components/hourly-pattern"
import { TopHashtags } from "@/components/top-hashtags"
import { KeyMetrics } from "@/components/key-metrics"
import { CityHeatmap } from "@/components/city-heatmap"

export default function Dashboard() {
  return (
    <div className="flex min-h-screen w-full flex-col">
      <header className="sticky top-0 z-10 border-b bg-background/95 backdrop-blur">
        <div className="container flex h-16 items-center justify-between py-4">
          <h1 className="text-xl font-bold">Pakistan Social Media Sentiment Tracker - 9th May 2023</h1>
        </div>
      </header>

      <main className="flex-1 space-y-6 p-4 md:p-8">
        <div className="mx-auto max-w-7xl space-y-6">
          {/* Search Form */}
          <SearchForm defaultQuery="Imran Khan 9th May" />

          {/* Overview Cards */}
          <SentimentOverview />

          {/* Key Metrics Row */}
          <div className="grid gap-4 md:grid-cols-3">
            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Sentiment Distribution</CardTitle>
                <CardDescription>Overall sentiment breakdown</CardDescription>
              </CardHeader>
              <CardContent>
                <SentimentDistribution />
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Key Metrics</CardTitle>
                <CardDescription>Important incident metrics</CardDescription>
              </CardHeader>
              <CardContent>
                <KeyMetrics />
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Top Hashtags</CardTitle>
                <CardDescription>Most used hashtags</CardDescription>
              </CardHeader>
              <CardContent>
                <TopHashtags />
              </CardContent>
            </Card>
          </div>

          {/* Timeline and Hourly Pattern */}
          <div className="grid gap-4 lg:grid-cols-2">
            <Card>
              <CardHeader>
                <CardTitle>Sentiment Timeline</CardTitle>
                <CardDescription>Track sentiment changes over time around May 9th incident</CardDescription>
              </CardHeader>
              <CardContent className="pt-2">
                <SentimentTimeline />
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Hourly Sentiment Pattern</CardTitle>
                <CardDescription>Sentiment patterns throughout the day on May 9th</CardDescription>
              </CardHeader>
              <CardContent className="pt-2">
                <HourlyPattern />
              </CardContent>
            </Card>
          </div>

          {/* Word Cloud and Region Map */}
          <div className="grid gap-4 lg:grid-cols-2">
            <Card>
              <CardHeader>
                <CardTitle>Popular Terms</CardTitle>
                <CardDescription>Most frequently mentioned terms in the conversation</CardDescription>
              </CardHeader>
              <CardContent className="pt-2">
                <SentimentWordcloud />
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Region-wise Sentiment</CardTitle>
                <CardDescription>Geographic distribution of sentiment across Pakistan</CardDescription>
              </CardHeader>
              <CardContent className="pt-2">
                <RegionMap />
              </CardContent>
            </Card>
          </div>

          {/* Engagement Metrics */}
          <Card>
            <CardHeader>
              <CardTitle>Engagement Metrics Over Time</CardTitle>
              <CardDescription>Track retweets, likes, and replies during the incident period</CardDescription>
            </CardHeader>
            <CardContent className="pt-2">
              <EngagementMetrics />
            </CardContent>
          </Card>

          {/* City Heatmap */}
          <Card>
            <CardHeader>
              <CardTitle>Top 5 Cities - Sentiment Heatmap</CardTitle>
              <CardDescription>
                Sentiment intensity and volume distribution across major Pakistani cities during the 9th May incident
              </CardDescription>
            </CardHeader>
            <CardContent className="pt-2">
              <CityHeatmap />
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  )
}
