"use client"

import { useEffect, useRef } from "react"

interface RegionData {
  id: string
  name: string
  sentiment: number // 0-100 scale, higher is more positive
  mentions: number
}

export function RegionMap() {
  const canvasRef = useRef<HTMLCanvasElement>(null)

  // In a real app, this data would come from the Twitter API and sentiment analysis
  const regionData: RegionData[] = [
    { id: "PB", name: "Punjab", sentiment: 38, mentions: 28450 },
    { id: "SD", name: "Sindh", sentiment: 45, mentions: 18300 },
    { id: "KP", name: "Khyber Pakhtunkhwa", sentiment: 52, mentions: 15400 },
    { id: "BL", name: "Balochistan", sentiment: 41, mentions: 4200 },
    { id: "ISB", name: "Islamabad", sentiment: 35, mentions: 12800 },
    { id: "LHR", name: "Lahore", sentiment: 40, mentions: 19200 },
    { id: "KHI", name: "Karachi", sentiment: 48, mentions: 16700 },
    { id: "RWP", name: "Rawalpindi", sentiment: 36, mentions: 8900 },
    { id: "FSL", name: "Faisalabad", sentiment: 42, mentions: 6800 },
    { id: "MLT", name: "Multan", sentiment: 39, mentions: 5600 },
  ]

  useEffect(() => {
    if (!canvasRef.current) return

    const canvas = canvasRef.current
    const ctx = canvas.getContext("2d")
    if (!ctx) return

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Draw a simple placeholder map
    ctx.fillStyle = "#f1f5f9"
    ctx.fillRect(50, 50, canvas.width - 100, canvas.height - 100)

    // Draw regions with sentiment colors
    const regionWidth = (canvas.width - 120) / 5
    const regionHeight = (canvas.height - 120) / 2

    regionData.slice(0, 10).forEach((region, i) => {
      const row = Math.floor(i / 5)
      const col = i % 5

      const x = 60 + col * regionWidth
      const y = 60 + row * regionHeight

      // Calculate color based on sentiment (red to green)
      const red = Math.floor(255 * (1 - region.sentiment / 100))
      const green = Math.floor(255 * (region.sentiment / 100))
      ctx.fillStyle = `rgb(${red}, ${green}, 100)`

      ctx.fillRect(x, y, regionWidth - 10, regionHeight - 10)

      // Add region label
      ctx.fillStyle = "#000000"
      ctx.font = "12px Arial"
      ctx.textAlign = "center"
      ctx.fillText(region.id, x + regionWidth / 2 - 5, y + regionHeight / 2)

      // Add sentiment value
      ctx.font = "10px Arial"
      ctx.fillText(`${region.sentiment}%`, x + regionWidth / 2 - 5, y + regionHeight / 2 + 15)
    })

    // Add legend
    ctx.font = "12px Arial"
    ctx.textAlign = "left"
    ctx.fillStyle = "#000000"
    ctx.fillText("Sentiment by Province/City", 60, 30)

    // Sentiment scale
    const gradientX = canvas.width - 200
    const gradientY = canvas.height - 30
    const gradientWidth = 150
    const gradientHeight = 15

    const gradient = ctx.createLinearGradient(gradientX, gradientY, gradientX + gradientWidth, gradientY)
    gradient.addColorStop(0, "rgb(255, 0, 100)")
    gradient.addColorStop(0.5, "rgb(255, 255, 0)")
    gradient.addColorStop(1, "rgb(0, 255, 100)")

    ctx.fillStyle = gradient
    ctx.fillRect(gradientX, gradientY, gradientWidth, gradientHeight)

    ctx.fillStyle = "#000000"
    ctx.textAlign = "center"
    ctx.fillText("0%", gradientX, gradientY + 25)
    ctx.fillText("50%", gradientX + gradientWidth / 2, gradientY + 25)
    ctx.fillText("100%", gradientX + gradientWidth, gradientY + 25)
  }, [regionData])

  return (
    <div className="space-y-4">
      <div className="relative h-[300px] w-full border rounded-md">
        <canvas ref={canvasRef} width={600} height={300} className="h-full w-full" />
      </div>

      <div className="grid grid-cols-2 gap-4 md:grid-cols-5">
        {regionData.slice(0, 5).map((region) => (
          <div key={region.id} className="text-center">
            <div className="font-medium">{region.name}</div>
            <div className="text-sm text-muted-foreground">{region.sentiment}% positive</div>
            <div className="text-xs text-muted-foreground">{region.mentions.toLocaleString()} mentions</div>
          </div>
        ))}
      </div>
    </div>
  )
}
