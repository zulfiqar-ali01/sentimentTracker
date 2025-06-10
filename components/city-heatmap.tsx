"use client"

import { useEffect, useRef, useState } from "react"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Badge } from "@/components/ui/badge"
import { MapPin, Users, MessageSquare, TrendingDown, TrendingUp, Thermometer } from "lucide-react"

interface CityData {
  name: string
  sentiment: number
  volume: number
  lat: number
  lng: number
  population: string
  keyEvents: string[]
  hourlyData: { hour: string; sentiment: number; volume: number }[]
}

export function CityHeatmap() {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const [selectedMetric, setSelectedMetric] = useState("sentiment")
  const [selectedCity, setSelectedCity] = useState<string | null>(null)
  const [showHeatmap, setShowHeatmap] = useState(true)

  // Top 5 Pakistani cities with actual coordinates
  const cityData: CityData[] = [
    {
      name: "Lahore",
      sentiment: 35,
      volume: 28450,
      lat: 31.5497,
      lng: 74.3436,
      population: "11.1M",
      keyEvents: ["Corps Commander House attacked", "Radio Pakistan building damaged", "Major protests"],
      hourlyData: [
        { hour: "10 AM", sentiment: 45, volume: 1200 },
        { hour: "12 PM", sentiment: 25, volume: 3500 },
        { hour: "2 PM", sentiment: 15, volume: 5200 },
        { hour: "4 PM", sentiment: 20, volume: 4800 },
        { hour: "6 PM", sentiment: 30, volume: 3200 },
      ],
    },
    {
      name: "Karachi",
      sentiment: 48,
      volume: 19200,
      lat: 24.8607,
      lng: 67.0011,
      population: "14.9M",
      keyEvents: ["Peaceful protests", "Limited incidents", "Strong police presence"],
      hourlyData: [
        { hour: "10 AM", sentiment: 52, volume: 800 },
        { hour: "12 PM", sentiment: 45, volume: 2100 },
        { hour: "2 PM", sentiment: 40, volume: 3800 },
        { hour: "4 PM", sentiment: 48, volume: 2900 },
        { hour: "6 PM", sentiment: 55, volume: 1500 },
      ],
    },
    {
      name: "Islamabad",
      sentiment: 32,
      volume: 15600,
      lat: 33.6844,
      lng: 73.0479,
      population: "1.1M",
      keyEvents: ["Imran Khan arrest location", "Heavy security", "Media restrictions"],
      hourlyData: [
        { hour: "10 AM", sentiment: 40, volume: 900 },
        { hour: "12 PM", sentiment: 20, volume: 2800 },
        { hour: "2 PM", sentiment: 25, volume: 3200 },
        { hour: "4 PM", sentiment: 35, volume: 2400 },
        { hour: "6 PM", sentiment: 40, volume: 1800 },
      ],
    },
    {
      name: "Rawalpindi",
      sentiment: 38,
      volume: 12800,
      lat: 33.5651,
      lng: 73.0169,
      population: "2.1M",
      keyEvents: ["Military installations nearby", "Controlled protests", "Curfew imposed"],
      hourlyData: [
        { hour: "10 AM", sentiment: 42, volume: 600 },
        { hour: "12 PM", sentiment: 30, volume: 1800 },
        { hour: "2 PM", sentiment: 28, volume: 2500 },
        { hour: "4 PM", sentiment: 40, volume: 1900 },
        { hour: "6 PM", sentiment: 45, volume: 1200 },
      ],
    },
    {
      name: "Peshawar",
      sentiment: 52,
      volume: 8900,
      lat: 34.0151,
      lng: 71.5249,
      population: "1.97M",
      keyEvents: ["Pro-Imran rallies", "Peaceful demonstrations", "Strong PTI support"],
      hourlyData: [
        { hour: "10 AM", sentiment: 58, volume: 400 },
        { hour: "12 PM", sentiment: 50, volume: 1200 },
        { hour: "2 PM", sentiment: 45, volume: 2100 },
        { hour: "4 PM", sentiment: 55, volume: 1800 },
        { hour: "6 PM", sentiment: 60, volume: 1000 },
      ],
    },
  ]

  // Convert lat/lng to canvas coordinates
  const latLngToCanvas = (lat: number, lng: number, canvasWidth: number, canvasHeight: number) => {
    // Pakistan bounds approximately
    const minLat = 23.5,
      maxLat = 37.0
    const minLng = 60.0,
      maxLng = 77.0

    const x = ((lng - minLng) / (maxLng - minLng)) * (canvasWidth - 100) + 50
    const y = ((maxLat - lat) / (maxLat - minLat)) * (canvasHeight - 100) + 50

    return { x, y }
  }

  const getHeatmapColor = (value: number, metric: string) => {
    if (metric === "sentiment") {
      if (value >= 60) return "#22c55e" // Green
      if (value >= 45) return "#eab308" // Yellow
      if (value >= 30) return "#f97316" // Orange
      return "#ef4444" // Red
    } else {
      const intensity = Math.min(value / 30000, 1)
      if (intensity >= 0.8) return "#1e40af" // Dark blue
      if (intensity >= 0.6) return "#3b82f6" // Blue
      if (intensity >= 0.4) return "#60a5fa" // Light blue
      return "#93c5fd" // Very light blue
    }
  }

  const getCircleSize = (value: number, metric: string) => {
    if (metric === "sentiment") {
      return Math.max(15, Math.min(45, (value / 100) * 40 + 15))
    } else {
      return Math.max(15, Math.min(45, (value / 30000) * 40 + 15))
    }
  }

  const drawHeatmapGradient = (
    ctx: CanvasRenderingContext2D,
    centerX: number,
    centerY: number,
    intensity: number,
    color: string,
  ) => {
    const radius = intensity * 80
    const gradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, radius)

    // Parse color and create gradient
    const alpha = intensity * 0.6
    if (color === "#ef4444") {
      // Red
      gradient.addColorStop(0, `rgba(239, 68, 68, ${alpha})`)
      gradient.addColorStop(1, `rgba(239, 68, 68, 0)`)
    } else if (color === "#f97316") {
      // Orange
      gradient.addColorStop(0, `rgba(249, 115, 22, ${alpha})`)
      gradient.addColorStop(1, `rgba(249, 115, 22, 0)`)
    } else if (color === "#eab308") {
      // Yellow
      gradient.addColorStop(0, `rgba(234, 179, 8, ${alpha})`)
      gradient.addColorStop(1, `rgba(234, 179, 8, 0)`)
    } else {
      // Green
      gradient.addColorStop(0, `rgba(34, 197, 94, ${alpha})`)
      gradient.addColorStop(1, `rgba(34, 197, 94, 0)`)
    }

    ctx.fillStyle = gradient
    ctx.beginPath()
    ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI)
    ctx.fill()
  }

  useEffect(() => {
    if (!canvasRef.current) return

    const canvas = canvasRef.current
    const ctx = canvas.getContext("2d")
    if (!ctx) return

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Draw Pakistan map background
    ctx.fillStyle = "#f8fafc"
    ctx.fillRect(0, 0, canvas.width, canvas.height)

    // Draw simplified Pakistan border
    ctx.strokeStyle = "#cbd5e1"
    ctx.lineWidth = 2
    ctx.beginPath()

    // Simplified Pakistan outline
    const pakistanOutline = [
      { lat: 37.0, lng: 74.0 }, // North
      { lat: 36.0, lng: 77.0 }, // Northeast
      { lat: 32.0, lng: 75.0 }, // East
      { lat: 29.0, lng: 73.0 }, // Southeast
      { lat: 24.0, lng: 68.0 }, // South
      { lat: 25.0, lng: 62.0 }, // Southwest
      { lat: 28.0, lng: 61.0 }, // West
      { lat: 34.0, lng: 69.0 }, // Northwest
    ]

    pakistanOutline.forEach((point, index) => {
      const coords = latLngToCanvas(point.lat, point.lng, canvas.width, canvas.height)
      if (index === 0) {
        ctx.moveTo(coords.x, coords.y)
      } else {
        ctx.lineTo(coords.x, coords.y)
      }
    })
    ctx.closePath()
    ctx.stroke()
    ctx.fillStyle = "#f1f5f9"
    ctx.fill()

    // Draw heatmap if enabled
    if (showHeatmap) {
      cityData.forEach((city) => {
        const coords = latLngToCanvas(city.lat, city.lng, canvas.width, canvas.height)
        const value = selectedMetric === "sentiment" ? city.sentiment : city.volume
        const color = getHeatmapColor(value, selectedMetric)
        const intensity = selectedMetric === "sentiment" ? value / 100 : Math.min(value / 30000, 1)

        drawHeatmapGradient(ctx, coords.x, coords.y, intensity, color)
      })
    }

    // Draw cities
    cityData.forEach((city) => {
      const coords = latLngToCanvas(city.lat, city.lng, canvas.width, canvas.height)
      const value = selectedMetric === "sentiment" ? city.sentiment : city.volume
      const color = getHeatmapColor(value, selectedMetric)
      const size = getCircleSize(value, selectedMetric)

      // Draw city circle with glow effect
      ctx.shadowColor = color
      ctx.shadowBlur = 10
      ctx.beginPath()
      ctx.arc(coords.x, coords.y, size / 2, 0, 2 * Math.PI)
      ctx.fillStyle = color
      ctx.fill()

      // White border
      ctx.shadowBlur = 0
      ctx.strokeStyle = "#ffffff"
      ctx.lineWidth = 3
      ctx.stroke()

      // Inner circle for selected city
      if (selectedCity === city.name) {
        ctx.beginPath()
        ctx.arc(coords.x, coords.y, size / 2 + 5, 0, 2 * Math.PI)
        ctx.strokeStyle = "#3b82f6"
        ctx.lineWidth = 3
        ctx.stroke()
      }

      // City label with background
      ctx.fillStyle = "rgba(255, 255, 255, 0.9)"
      ctx.fillRect(coords.x - 25, coords.y + size / 2 + 5, 50, 30)
      ctx.strokeStyle = "#e5e7eb"
      ctx.lineWidth = 1
      ctx.strokeRect(coords.x - 25, coords.y + size / 2 + 5, 50, 30)

      // City name
      ctx.fillStyle = "#374151"
      ctx.font = "bold 11px Arial"
      ctx.textAlign = "center"
      ctx.fillText(city.name, coords.x, coords.y + size / 2 + 18)

      // Value
      ctx.font = "9px Arial"
      ctx.fillStyle = "#6b7280"
      const displayValue = selectedMetric === "sentiment" ? `${value}%` : `${(value / 1000).toFixed(1)}K`
      ctx.fillText(displayValue, coords.x, coords.y + size / 2 + 30)
    })

    // Add title and legend
    ctx.fillStyle = "#1f2937"
    ctx.font = "bold 16px Arial"
    ctx.textAlign = "left"
    ctx.fillText(`Pakistan Cities - ${selectedMetric === "sentiment" ? "Sentiment" : "Volume"} Heatmap`, 20, 30)

    // Legend
    const legendY = canvas.height - 60
    const legendItems =
      selectedMetric === "sentiment"
        ? [
            { color: "#ef4444", label: "Very Negative (0-30%)" },
            { color: "#f97316", label: "Negative (30-45%)" },
            { color: "#eab308", label: "Neutral (45-60%)" },
            { color: "#22c55e", label: "Positive (60%+)" },
          ]
        : [
            { color: "#93c5fd", label: "Low (0-10K)" },
            { color: "#60a5fa", label: "Medium (10-20K)" },
            { color: "#3b82f6", label: "High (20-25K)" },
            { color: "#1e40af", label: "Very High (25K+)" },
          ]

    legendItems.forEach((item, index) => {
      const x = 20 + index * 120
      ctx.fillStyle = item.color
      ctx.fillRect(x, legendY, 15, 15)
      ctx.fillStyle = "#374151"
      ctx.font = "10px Arial"
      ctx.fillText(item.label, x + 20, legendY + 12)
    })
  }, [selectedMetric, cityData, selectedCity, showHeatmap])

  const handleCityClick = (cityName: string) => {
    setSelectedCity(selectedCity === cityName ? null : cityName)
  }

  const selectedCityData = cityData.find((city) => city.name === selectedCity)

  return (
    <div className="space-y-6">
      {/* Controls */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center space-x-4">
          <Select value={selectedMetric} onValueChange={setSelectedMetric}>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Select metric" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="sentiment">Sentiment Intensity</SelectItem>
              <SelectItem value="volume">Message Volume</SelectItem>
            </SelectContent>
          </Select>

          <button
            onClick={() => setShowHeatmap(!showHeatmap)}
            className={`flex items-center space-x-2 px-3 py-2 rounded-md text-sm font-medium transition-colors ${
              showHeatmap
                ? "bg-blue-100 text-blue-700 hover:bg-blue-200"
                : "bg-gray-100 text-gray-700 hover:bg-gray-200"
            }`}
          >
            <Thermometer className="h-4 w-4" />
            <span>Heatmap {showHeatmap ? "ON" : "OFF"}</span>
          </button>
        </div>

        <div className="flex items-center space-x-2 text-sm text-gray-600">
          <MapPin className="h-4 w-4" />
          <span>Click on cities for detailed analysis</span>
        </div>
      </div>

      {/* Heatmap */}
      <div className="relative border rounded-lg overflow-hidden bg-white shadow-lg">
        <canvas
          ref={canvasRef}
          width={800}
          height={500}
          className="w-full cursor-pointer"
          onClick={(e) => {
            const rect = e.currentTarget.getBoundingClientRect()
            const x = ((e.clientX - rect.left) / rect.width) * 800
            const y = ((e.clientY - rect.top) / rect.height) * 500

            // Find clicked city
            const clickedCity = cityData.find((city) => {
              const coords = latLngToCanvas(city.lat, city.lng, 800, 500)
              const distance = Math.sqrt(Math.pow(x - coords.x, 2) + Math.pow(y - coords.y, 2))
              return distance <= 30
            })

            if (clickedCity) {
              handleCityClick(clickedCity.name)
            }
          }}
        />
      </div>

      {/* City Statistics Grid */}
      <div className="grid gap-4 md:grid-cols-5">
        {cityData.map((city) => (
          <div
            key={city.name}
            className={`p-4 border rounded-lg cursor-pointer transition-all hover:shadow-lg ${
              selectedCity === city.name
                ? "border-blue-500 bg-blue-50 shadow-md"
                : "border-gray-200 hover:border-gray-300"
            }`}
            onClick={() => handleCityClick(city.name)}
          >
            <div className="flex items-center justify-between mb-3">
              <h3 className="font-semibold text-gray-900">{city.name}</h3>
              <div
                className="w-4 h-4 rounded-full border-2 border-white shadow-sm"
                style={{
                  backgroundColor: getHeatmapColor(
                    selectedMetric === "sentiment" ? city.sentiment : city.volume,
                    selectedMetric,
                  ),
                }}
              ></div>
            </div>

            <div className="space-y-3">
              <div className="flex items-center justify-between text-sm">
                <span className="text-gray-600">Sentiment</span>
                <div className="flex items-center space-x-1">
                  {city.sentiment > 50 ? (
                    <TrendingUp className="h-3 w-3 text-green-500" />
                  ) : (
                    <TrendingDown className="h-3 w-3 text-red-500" />
                  )}
                  <span className={`font-medium ${city.sentiment > 50 ? "text-green-600" : "text-red-600"}`}>
                    {city.sentiment}%
                  </span>
                </div>
              </div>

              <div className="flex items-center justify-between text-sm">
                <span className="text-gray-600">Volume</span>
                <div className="flex items-center space-x-1">
                  <MessageSquare className="h-3 w-3 text-blue-500" />
                  <span className="font-medium text-blue-600">{(city.volume / 1000).toFixed(1)}K</span>
                </div>
              </div>

              <div className="flex items-center justify-between text-sm">
                <span className="text-gray-600">Population</span>
                <div className="flex items-center space-x-1">
                  <Users className="h-3 w-3 text-purple-500" />
                  <span className="font-medium text-purple-600">{city.population}</span>
                </div>
              </div>

              {/* Sentiment bar */}
              <div className="w-full h-2 bg-gray-200 rounded-full">
                <div
                  className={`h-2 rounded-full ${city.sentiment > 50 ? "bg-green-500" : "bg-red-500"}`}
                  style={{ width: `${city.sentiment}%` }}
                ></div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Selected City Details */}
      {selectedCityData && (
        <div className="border rounded-lg p-6 bg-gradient-to-r from-blue-50 to-indigo-50">
          <div className="flex items-center space-x-3 mb-4">
            <div
              className="w-6 h-6 rounded-full border-2 border-white shadow-sm"
              style={{
                backgroundColor: getHeatmapColor(
                  selectedMetric === "sentiment" ? selectedCityData.sentiment : selectedCityData.volume,
                  selectedMetric,
                ),
              }}
            ></div>
            <h3 className="text-lg font-semibold text-gray-900">{selectedCityData.name} - Detailed Analysis</h3>
          </div>

          <div className="grid gap-6 md:grid-cols-2">
            {/* Key Events */}
            <div>
              <h4 className="font-medium text-gray-700 mb-3 flex items-center">
                <MapPin className="h-4 w-4 mr-2" />
                Key Events on May 9th
              </h4>
              <div className="space-y-3">
                {selectedCityData.keyEvents.map((event, index) => (
                  <div key={index} className="flex items-start space-x-3 p-3 bg-white rounded-lg border">
                    <div className="w-2 h-2 rounded-full bg-blue-500 mt-2 flex-shrink-0"></div>
                    <span className="text-sm text-gray-700">{event}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Hourly Pattern */}
            <div>
              <h4 className="font-medium text-gray-700 mb-3 flex items-center">
                <Thermometer className="h-4 w-4 mr-2" />
                Hourly Sentiment Pattern
              </h4>
              <div className="space-y-3">
                {selectedCityData.hourlyData.map((hour, index) => (
                  <div key={index} className="p-3 bg-white rounded-lg border">
                    <div className="flex items-center justify-between text-sm mb-2">
                      <span className="font-medium text-gray-700">{hour.hour}</span>
                      <div className="flex items-center space-x-2">
                        <span className={`font-medium ${hour.sentiment > 50 ? "text-green-600" : "text-red-600"}`}>
                          {hour.sentiment}%
                        </span>
                        <Badge variant="secondary" className="text-xs">
                          {(hour.volume / 1000).toFixed(1)}K
                        </Badge>
                      </div>
                    </div>
                    <div className="w-full h-2 bg-gray-200 rounded-full">
                      <div
                        className={`h-2 rounded-full ${hour.sentiment > 50 ? "bg-green-500" : "bg-red-500"}`}
                        style={{ width: `${hour.sentiment}%` }}
                      ></div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
