"use client"

import { useEffect, useRef, useState } from "react"

interface WordCloudWord {
  text: string
  urdu?: string
  value: number
  sentiment: "positive" | "negative" | "neutral"
}

export function SentimentWordcloud() {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const [activeTab, setActiveTab] = useState("all")
  const [showUrdu, setShowUrdu] = useState(true)

  // Popular terms from 9th May 2023 with Urdu translations
  const words: WordCloudWord[] = [
    { text: "ImranKhan", urdu: "عمران خان", value: 95, sentiment: "positive" },
    { text: "9thMay", urdu: "نو مئی", value: 88, sentiment: "negative" },
    { text: "Violence", urdu: "تشدد", value: 82, sentiment: "negative" },
    { text: "Arrest", urdu: "گرفتاری", value: 78, sentiment: "negative" },
    { text: "PTI", urdu: "پی ٹی آئی", value: 75, sentiment: "positive" },
    { text: "Justice", urdu: "انصاف", value: 68, sentiment: "positive" },
    { text: "Pakistan", urdu: "پاکستان", value: 65, sentiment: "neutral" },
    { text: "Protests", urdu: "احتجاج", value: 62, sentiment: "neutral" },
    { text: "Extremism", urdu: "انتہا پسندی", value: 58, sentiment: "negative" },
    { text: "Democracy", urdu: "جمہوریت", value: 55, sentiment: "positive" },
    { text: "Corruption", urdu: "بدعنوانی", value: 52, sentiment: "negative" },
    { text: "Military", urdu: "فوج", value: 48, sentiment: "negative" },
    { text: "Supporters", urdu: "حامی", value: 45, sentiment: "positive" },
    { text: "Lahore", urdu: "لاہور", value: 42, sentiment: "neutral" },
    { text: "Islamabad", urdu: "اسلام آباد", value: 38, sentiment: "neutral" },
    { text: "Karachi", urdu: "کراچی", value: 35, sentiment: "neutral" },
    { text: "Vandalism", urdu: "توڑ پھوڑ", value: 32, sentiment: "negative" },
    { text: "Peaceful", urdu: "پرامن", value: 28, sentiment: "positive" },
    { text: "Rights", urdu: "حقوق", value: 25, sentiment: "positive" },
    { text: "Chaos", urdu: "افراتفری", value: 22, sentiment: "negative" },
    { text: "Leader", urdu: "رہنما", value: 35, sentiment: "positive" },
    { text: "Court", urdu: "عدالت", value: 30, sentiment: "neutral" },
    { text: "Freedom", urdu: "آزادی", value: 28, sentiment: "positive" },
    { text: "Attack", urdu: "حملہ", value: 40, sentiment: "negative" },
  ]

  useEffect(() => {
    if (!canvasRef.current) return

    const canvas = canvasRef.current
    const ctx = canvas.getContext("2d")
    if (!ctx) return

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Filter words based on active tab
    const filteredWords = activeTab === "all" ? words : words.filter((word) => word.sentiment === activeTab)

    // Simple word cloud rendering with Urdu support
    ctx.textAlign = "center"
    ctx.textBaseline = "middle"

    const centerX = canvas.width / 2
    const centerY = canvas.height / 2

    filteredWords.forEach((word, i) => {
      const angle = (i / filteredWords.length) * Math.PI * 2
      const radius = 80 + Math.random() * 60
      const x = centerX + Math.cos(angle) * radius
      const y = centerY + Math.sin(angle) * radius

      const fontSize = Math.max(12, Math.min(36, word.value / 3))

      // Set color based on sentiment
      if (word.sentiment === "positive") {
        ctx.fillStyle = "#22c55e" // green
      } else if (word.sentiment === "negative") {
        ctx.fillStyle = "#ef4444" // red
      } else {
        ctx.fillStyle = "#94a3b8" // gray
      }

      // Display English text
      ctx.font = `${fontSize}px Arial`
      ctx.fillText(word.text, x, y - (showUrdu && word.urdu ? 8 : 0))

      // Display Urdu text if available and enabled
      if (showUrdu && word.urdu) {
        ctx.font = `${Math.max(10, fontSize - 4)}px Arial`
        ctx.fillStyle = ctx.fillStyle // Keep same color but slightly transparent
        ctx.globalAlpha = 0.8
        ctx.fillText(word.urdu, x, y + 12)
        ctx.globalAlpha = 1
      }
    })
  }, [activeTab, words, showUrdu])

  return (
    <div className="space-y-4">
      {/* Controls */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div className="flex space-x-2">
          <button
            onClick={() => setActiveTab("all")}
            className={`px-3 py-1 rounded text-sm ${
              activeTab === "all"
                ? "bg-primary text-primary-foreground"
                : "bg-secondary text-secondary-foreground hover:bg-secondary/80"
            }`}
          >
            All Terms
          </button>
          <button
            onClick={() => setActiveTab("positive")}
            className={`px-3 py-1 rounded text-sm ${
              activeTab === "positive"
                ? "bg-green-500 text-white"
                : "bg-secondary text-secondary-foreground hover:bg-secondary/80"
            }`}
          >
            Positive
          </button>
          <button
            onClick={() => setActiveTab("negative")}
            className={`px-3 py-1 rounded text-sm ${
              activeTab === "negative"
                ? "bg-red-500 text-white"
                : "bg-secondary text-secondary-foreground hover:bg-secondary/80"
            }`}
          >
            Negative
          </button>
          <button
            onClick={() => setActiveTab("neutral")}
            className={`px-3 py-1 rounded text-sm ${
              activeTab === "neutral"
                ? "bg-gray-500 text-white"
                : "bg-secondary text-secondary-foreground hover:bg-secondary/80"
            }`}
          >
            Neutral
          </button>
        </div>

        <button
          onClick={() => setShowUrdu(!showUrdu)}
          className={`px-3 py-1 rounded text-sm ${
            showUrdu ? "bg-blue-500 text-white" : "bg-secondary text-secondary-foreground hover:bg-secondary/80"
          }`}
        >
          {showUrdu ? "اردو ON" : "اردو OFF"}
        </button>
      </div>

      {/* Word Cloud Canvas */}
      <div className="relative h-[300px] w-full">
        <canvas ref={canvasRef} width={600} height={300} className="h-full w-full" />
      </div>

      {/* Legend */}
      <div className="flex justify-center space-x-6 text-sm">
        <div className="flex items-center">
          <div className="mr-1 h-3 w-3 rounded-full bg-green-500"></div>
          <span>Positive</span>
        </div>
        <div className="flex items-center">
          <div className="mr-1 h-3 w-3 rounded-full bg-red-500"></div>
          <span>Negative</span>
        </div>
        <div className="flex items-center">
          <div className="mr-1 h-3 w-3 rounded-full bg-gray-400"></div>
          <span>Neutral</span>
        </div>
      </div>

      {/* Popular Terms List */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
        {words.slice(0, 8).map((word, index) => (
          <div key={index} className="flex flex-col items-center p-2 bg-gray-50 rounded">
            <span className="font-medium">{word.text}</span>
            {word.urdu && <span className="text-gray-600 mt-1">{word.urdu}</span>}
            <span
              className={`text-xs mt-1 ${
                word.sentiment === "positive"
                  ? "text-green-600"
                  : word.sentiment === "negative"
                    ? "text-red-600"
                    : "text-gray-600"
              }`}
            >
              {word.value} mentions
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}
