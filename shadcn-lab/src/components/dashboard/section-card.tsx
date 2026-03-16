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
  surface?: "subtle" | "outlined"
  compactHeader?: boolean
  className?: string
  contentClassName?: string
  children?: ReactNode
}

export function SectionCard({
  title,
  description,
  action,
  surface = "subtle",
  compactHeader = false,
  className,
  contentClassName,
  children,
}: SectionCardProps) {
  const hasDescription = Boolean(description)

  return (
    <Card
      className={cn(
        "rounded-[16px] shadow-none",
        surface === "outlined"
          ? "border border-border/80 bg-white ring-0"
          : "border-0 bg-card ring-0",
        className
      )}
    >
      <CardHeader
        className={cn(
          compactHeader ? "px-6 pb-0 pt-[11px]" : "px-6 pb-0 pt-[13px]",
          hasDescription ? "gap-2.5" : "gap-1"
        )}
      >
        <div className={cn(hasDescription ? "space-y-1.5" : "space-y-1")}>
          <CardTitle
            className={cn(
              "font-[family:var(--font-brand)] font-semibold text-foreground",
              compactHeader
                ? "text-[18px] leading-[1.08] tracking-[-0.03em]"
                : "text-[22px] leading-[1.08] tracking-[-0.04em]"
            )}
          >
            {title}
          </CardTitle>
          {description ? (
            <CardDescription className="text-[12px] leading-[1.55] text-muted-foreground/88">
              {description}
            </CardDescription>
          ) : null}
        </div>
        {action ? <CardAction>{action}</CardAction> : null}
      </CardHeader>
      <Separator
        className={cn(
          "bg-border/60",
          compactHeader
            ? hasDescription
              ? "mt-2"
              : "mt-1.5"
            : hasDescription
              ? "mt-2.5"
              : "mt-2"
        )}
      />
      {children !== undefined ? (
        <CardContent
          className={cn(
            compactHeader ? "px-6 pb-6 pt-[10px]" : "px-6 pb-6 pt-[12px]",
            contentClassName
          )}
        >
          {children}
        </CardContent>
      ) : null}
    </Card>
  )
}
