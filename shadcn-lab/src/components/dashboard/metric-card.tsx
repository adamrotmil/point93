import * as React from "react"
import type { LucideIcon } from "lucide-react"

import { Card, CardContent } from "@/components/ui/card"
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
import { cn } from "@/lib/utils"

type MetricCardProps = {
  icon: LucideIcon
  value: string
  label: string
  tooltip?: string
  sparkline?: readonly number[]
  className?: string
}

export function MetricCard({
  icon: _icon,
  value,
  label,
  tooltip,
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
          {tooltip ? (
            <Tooltip>
              <TooltipTrigger
                render={
                  <p className="w-fit cursor-default text-[12.5px] font-medium leading-5 text-foreground/92" />
                }
              >
                {label}
              </TooltipTrigger>
              <TooltipContent
                side="top"
                align="start"
                className="max-w-[220px] text-[11px] leading-[1.45]"
              >
                {tooltip}
              </TooltipContent>
            </Tooltip>
          ) : (
            <p className="text-[12.5px] font-medium leading-5 text-foreground/92">
              {label}
            </p>
          )}
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
  const id = React.useId().replace(/:/g, "")
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
  const areaClipId = `metric-sparkline-area-${id}`
  const dotPatternId = `metric-sparkline-dots-${id}`

  return (
    <div className="mt-3.5">
      <svg
        viewBox={`0 0 ${width} ${height}`}
        className="h-11 w-full overflow-visible"
        aria-hidden="true"
      >
        <defs>
          <clipPath id={areaClipId}>
            <polygon points={areaPoints} />
          </clipPath>
          <pattern
            id={dotPatternId}
            width="7"
            height="7"
            patternUnits="userSpaceOnUse"
          >
            <circle cx="1.7" cy="1.7" r="0.8" fill="rgba(37,99,235,0.24)" />
          </pattern>
        </defs>
        <polygon points={areaPoints} fill="rgba(37,99,235,0.08)" stroke="none" />
        <rect
          x="0"
          y="0"
          width={width}
          height={height}
          fill={`url(#${dotPatternId})`}
          clipPath={`url(#${areaClipId})`}
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
