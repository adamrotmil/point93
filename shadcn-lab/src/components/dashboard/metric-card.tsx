import type { LucideIcon } from "lucide-react"

import { Card, CardContent } from "@/components/ui/card"
import { cn } from "@/lib/utils"

type MetricCardProps = {
  icon: LucideIcon
  value: string
  label: string
  sparkline?: readonly number[]
  className?: string
}

export function MetricCard({
  icon: _icon,
  value,
  label,
  sparkline,
  className,
}: MetricCardProps) {
  return (
    <Card
      size="sm"
      className={cn(
        "rounded-[16px] border-0 bg-[#eef1f4] py-0 shadow-none ring-0",
        className
      )}
    >
      <CardContent className="px-5 py-[18px]">
        <div className="min-w-0">
          <p className="text-[12.5px] font-medium leading-5 text-foreground/92">
            {label}
          </p>
          <p className="mt-2.5 font-[family:var(--font-display)] text-[1.66rem] leading-none font-normal tracking-[-0.03em] text-foreground/92">
            {value}
          </p>
          {sparkline ? <MetricSparkline data={sparkline} /> : null}
        </div>
      </CardContent>
    </Card>
  )
}

function MetricSparkline({ data }: { data: readonly number[] }) {
  const width = 168
  const height = 44
  const padding = 4
  const min = Math.min(...data)
  const max = Math.max(...data)
  const range = max - min || 1

  const points = data
    .map((value, index) => {
      const x =
        padding +
        (index * (width - padding * 2)) / Math.max(data.length - 1, 1)
      const y =
        height -
        padding -
        ((value - min) / range) * (height - padding * 2)

      return `${x.toFixed(2)},${y.toFixed(2)}`
    })
    .join(" ")

  const areaPoints = `${padding},${height - padding} ${points} ${
    width - padding
  },${height - padding}`

  return (
    <div className="mt-3.5">
      <svg
        viewBox={`0 0 ${width} ${height}`}
        className="h-11 w-full overflow-visible"
        aria-hidden="true"
      >
        <polyline
          points={areaPoints}
          fill="rgba(37,99,235,0.08)"
          stroke="none"
        />
        <polyline
          points={points}
          fill="none"
          stroke="rgba(37,99,235,0.86)"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
    </div>
  )
}
