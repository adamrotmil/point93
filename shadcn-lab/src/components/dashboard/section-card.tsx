import type { ReactNode } from "react"

import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"
import { cn } from "@/lib/utils"

type SectionCardProps = {
  title: string
  description?: string
  action?: ReactNode
  className?: string
  contentClassName?: string
  children: ReactNode
}

export function SectionCard({
  title,
  description,
  action,
  className,
  contentClassName,
  children,
}: SectionCardProps) {
  return (
    <Card
      className={cn(
        "rounded-[18px] border border-border/70 bg-card/96 shadow-[0_18px_34px_-32px_rgba(15,23,42,0.18)]",
        className
      )}
    >
      <CardHeader className="gap-3 px-6 pb-0 pt-5">
        <div className="space-y-1.5">
          <CardTitle className="text-[15px] font-semibold tracking-[-0.01em] text-foreground">
            {title}
          </CardTitle>
          {description ? (
            <CardDescription className="text-[13px] leading-5 text-muted-foreground">
              {description}
            </CardDescription>
          ) : null}
        </div>
        {action ? <CardAction>{action}</CardAction> : null}
      </CardHeader>
      <div className="px-6 pt-4">
        <Separator className="bg-border/80" />
      </div>
      <CardContent className={cn("px-6 pb-6 pt-5", contentClassName)}>
        {children}
      </CardContent>
    </Card>
  )
}
