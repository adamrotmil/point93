import type { LucideIcon } from "lucide-react"

import { Card, CardContent } from "@/components/ui/card"
import { cn } from "@/lib/utils"

type MetricCardProps = {
  icon: LucideIcon
  value: string
  label: string
  className?: string
}

export function MetricCard({
  icon: Icon,
  value,
  label,
  className,
}: MetricCardProps) {
  return (
    <Card
      size="sm"
      className={cn(
        "rounded-[16px] border border-border/70 bg-card/96 py-0 shadow-[0_10px_20px_-20px_rgba(15,23,42,0.18)]",
        className
      )}
    >
      <CardContent className="flex items-start gap-3 px-5 py-4">
        <div className="grid size-10 shrink-0 place-items-center rounded-full bg-primary/8 text-primary">
          <Icon className="size-4 stroke-[1.9]" />
        </div>
        <div className="min-w-0 pt-0.5">
          <p className="text-[1.55rem] leading-none font-semibold tracking-[-0.02em] text-foreground">
            {value}
          </p>
          <p className="mt-2 text-sm leading-5 text-muted-foreground">
            {label}
          </p>
        </div>
      </CardContent>
    </Card>
  )
}
