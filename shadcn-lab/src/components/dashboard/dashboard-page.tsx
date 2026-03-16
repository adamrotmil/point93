import * as React from "react"
import {
  ArrowRight,
  BarChart3,
  BookOpenText,
  ChevronLeft,
  ChevronRight,
  Gauge,
  MessageSquare,
  Sparkles,
  Star,
  Target,
  Trophy,
  Workflow,
} from "lucide-react"
import {
  PolarAngleAxis,
  PolarGrid,
  Radar as RechartsRadar,
  RadarChart,
} from "recharts"

import { MetricCard } from "@/components/dashboard/metric-card"
import { SectionCard } from "@/components/dashboard/section-card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
  type ChartConfig,
} from "@/components/ui/chart"
import {
  AppSidebar,
} from "@/components/app-sidebar"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
  useSidebar,
} from "@/components/ui/sidebar"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { cn } from "@/lib/utils"

const RIGHT_RAIL_WIDTH = 340
const RIGHT_RAIL_STAGE_CLASS =
  "rounded-[18px] border border-border/75 bg-[linear-gradient(180deg,rgba(245,248,252,0.98),rgba(250,252,254,1))] px-4 py-4 shadow-[inset_0_1px_0_rgba(255,255,255,0.8)]"

const metricCards = [
  {
    icon: Gauge,
    value: "68",
    label: "Overall Score",
    sparkline: [42, 45, 47, 52, 56, 58, 61, 65, 68],
  },
  {
    icon: BarChart3,
    value: "Top 23%",
    label: "Performance",
    sparkline: [11, 13, 15, 16, 18, 20, 22, 21, 23],
  },
  {
    icon: Trophy,
    value: "8 pts",
    label: "Gap to Top 5%",
    sparkline: [18, 17, 16, 15, 14, 12, 11, 10, 8],
  },
  {
    icon: Target,
    value: "10 pts",
    label: "Gap to Average",
    sparkline: [22, 20, 18, 16, 15, 13, 12, 11, 10],
  },
  { icon: BookOpenText, value: "4/18", label: "Modules Completed" },
] as const

const scoreRadarData = [
  { category: "Professional", top5: 72, average: 38 },
  { category: "Fees", top5: 61, average: 33 },
  { category: "Client Service", top5: 78, average: 47 },
  { category: "Planning", top5: 67, average: 35 },
  { category: "Investment", top5: 74, average: 42 },
  { category: "Firm Platform", top5: 58, average: 31 },
] as const

const scoreRadarConfig = {
  top5: {
    label: "Top 5%",
    color: "var(--chart-1)",
  },
  average: {
    label: "Industry average",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig

const intelligenceRows = [
  { name: "NextGen Ready", value: "8", impact: "Highest impact" },
  { name: "Client Referrals", value: "0", impact: "High impact" },
  { name: "PitchPerfect", value: "0", impact: "High impact" },
  { name: "COI Referrals", value: "0", impact: "Highest impact" },
] as const

const profileRows = [
  { name: "NextGen Ready", value: 0 },
  { name: "Client Referrals", value: 0 },
] as const

const moduleCards = [
  {
    title: "Level Scorecard",
  },
  {
    title: "Performance",
  },
  {
    title: "Datapoint Scoring",
  },
] as const

export function Point93DashboardPage() {
  return (
    <SidebarProvider defaultOpen>
      <AppSidebar />
      <DashboardShell />
    </SidebarProvider>
  )
}

function DashboardShell() {
  const [rightRailCollapsed, setRightRailCollapsed] = React.useState(false)
  const { state, toggleSidebar } = useSidebar()
  const leftSidebarCollapsed = state === "collapsed"

  return (
    <SidebarInset className="bg-transparent">
      <div className="min-h-svh bg-background">
        <header className="bg-transparent">
          <div
            className={cn(
              "px-5 pb-5 pt-7 sm:px-8 sm:pb-6 sm:pt-8",
              !rightRailCollapsed && "xl:pr-[23rem]"
            )}
          >
            <div className="mx-auto flex max-w-[1120px] items-center gap-4">
              <div className="flex items-center gap-3">
                <SidebarTrigger
                  variant="outline"
                  size="icon-sm"
                  className="rounded-full md:hidden"
                />
                <div>
                  <h1 className="font-[family:var(--font-brand)] text-[2.18rem] font-normal tracking-[-0.03em] text-foreground">
                    Welcome back, Brendon
                  </h1>
                </div>
              </div>
            </div>
          </div>
        </header>

        <DesktopPanelHandle
          side="left"
          collapsed={leftSidebarCollapsed}
          onClick={toggleSidebar}
        />

        <DesktopPanelHandle
          side="right"
          collapsed={rightRailCollapsed}
          onClick={() => setRightRailCollapsed((value) => !value)}
          rightRailWidth={rightRailCollapsed ? 0 : RIGHT_RAIL_WIDTH}
        />

        <main
          className={cn(
            "relative px-5 pb-8 pt-5 sm:px-8 sm:pb-10 sm:pt-6",
            !rightRailCollapsed && "xl:pr-[23rem]"
          )}
        >
          <div className="mx-auto max-w-[1120px] space-y-6">
            <section className="overflow-hidden rounded-[18px] bg-[linear-gradient(135deg,rgba(37,99,235,0.98),rgba(29,78,216,0.97)_52%,rgba(22,61,186,1)_100%)] px-6 py-6 shadow-[0_26px_44px_-32px_rgba(29,78,216,0.55)]">
              <div className="max-w-2xl">
                <h2 className="font-[family:var(--font-brand)] text-[1.3rem] font-medium tracking-[-0.024em] text-white">
                  Start Your Assessment
                </h2>
                <p className="mt-2 max-w-[34rem] text-[12.5px] leading-[1.55] text-white/78">
                  Complete your first module to unlock your scores and surface
                  the priorities that matter most for your business.
                </p>
                <Button
                  size="lg"
                  className="mt-5 rounded-full bg-white px-5 text-primary hover:bg-white/96"
                >
                  Begin First Module
                  <ArrowRight className="size-4" />
                </Button>
              </div>
            </section>

              <section className="grid gap-4 lg:grid-cols-2 2xl:grid-cols-5">
                {metricCards.map((card) => (
                  <MetricCard key={card.label} {...card} />
                ))}
              </section>

              <section className="grid gap-6 xl:grid-cols-[minmax(0,1fr)_320px]">
                <ScoreSummaryCard />
                <div className="grid gap-4 xl:grid-cols-1">
                  {moduleCards.map((card) => (
                    <SectionCard
                      key={card.title}
                      title={card.title}
                      surface="outlined"
                      className="min-h-[180px]"
                      contentClassName="flex h-full items-center justify-center"
                    >
                      <div className="flex w-full flex-col items-center justify-center gap-4 py-1">
                        <div className="grid size-12 place-items-center rounded-full bg-muted text-muted-foreground/75">
                          <BookOpenText className="size-5 stroke-[1.7]" />
                        </div>
                        <Button
                          variant="secondary"
                          size="sm"
                          className="px-3"
                        >
                          Start First Module
                        </Button>
                      </div>
                    </SectionCard>
                  ))}
                </div>
              </section>

            <SectionCard
              title="Strengths / Weaknesses"
              description="Complete modules to see your strengths and areas needing attention."
            >
              <div className="rounded-[16px] bg-white px-5 py-8 text-sm leading-6 text-muted-foreground">
                Your first assessment will unlock a clearer read on what is
                already working well and what should change next.
              </div>
            </SectionCard>

            <section className="grid gap-6 xl:grid-cols-[minmax(0,1.25fr)_minmax(0,0.9fr)]">
              <BusinessIntelligenceCard />
              <FocusAreasCard />
            </section>
          </div>
          <DashboardRightRail collapsed={rightRailCollapsed} />
        </main>

        <Button
          variant="outline"
          size="sm"
          className="fixed bottom-6 right-6 z-40 rounded-full border-border bg-white/96 shadow-[0_10px_24px_-18px_rgba(15,23,42,0.35)] backdrop-blur-sm"
        >
          <MessageSquare className="size-4" />
          Leave Feedback
        </Button>
      </div>
    </SidebarInset>
  )
}

function DesktopPanelHandle({
  side,
  collapsed,
  onClick,
  rightRailWidth = 0,
}: {
  side: "left" | "right"
  collapsed: boolean
  onClick: () => void
  rightRailWidth?: number
}) {
  const isLeft = side === "left"

  return (
    <Button
      variant="outline"
      size="icon-sm"
      className={
        isLeft
          ? "fixed top-1/2 z-30 hidden h-12 w-6 -translate-y-1/2 rounded-r-md rounded-l-none border-border bg-white text-muted-foreground shadow-[0_4px_12px_-12px_rgba(15,23,42,0.22)] md:flex"
          : "fixed top-1/2 z-30 hidden h-12 w-6 -translate-y-1/2 rounded-l-md rounded-r-none border-border bg-white text-muted-foreground shadow-[0_4px_12px_-12px_rgba(15,23,42,0.22)] xl:flex"
      }
      onClick={onClick}
      aria-label={
        isLeft
          ? collapsed
            ? "Expand navigation panel"
            : "Collapse navigation panel"
          : collapsed
            ? "Expand insights rail"
            : "Collapse insights rail"
      }
      style={
        isLeft
          ? {
              left: collapsed ? "3rem" : "16rem",
            }
          : {
              right: rightRailWidth === 0 ? "0px" : `${rightRailWidth}px`,
            }
      }
    >
      {isLeft ? (
        collapsed ? (
          <ChevronRight className="size-4" />
        ) : (
          <ChevronLeft className="size-4" />
        )
      ) : collapsed ? (
        <ChevronLeft className="size-4" />
      ) : (
        <ChevronRight className="size-4" />
      )}
    </Button>
  )
}
              

function ScoreSummaryCard() {
  return (
    <SectionCard
      title="How You Compare"
      surface="outlined"
      className="min-h-[460px]"
    >
      <div className="space-y-5">
        <div className="flex flex-wrap items-center gap-x-5 gap-y-2 text-[12px] text-muted-foreground">
          <div className="flex items-center gap-2">
            <span className="size-2.5 rounded-full bg-primary shadow-[0_0_0_3px_rgba(37,99,235,0.12)]" />
            <span>You</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="size-2.5 rounded-full bg-[color:var(--chart-1)]" />
            <span>Top 5%</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="size-2.5 rounded-full bg-[color:var(--chart-2)]" />
            <span>Industry average</span>
          </div>
        </div>
        <div className="relative rounded-[20px] border border-border/75 bg-[linear-gradient(180deg,rgba(245,248,252,0.98),rgba(250,252,254,1))] px-5 py-6 shadow-[inset_0_1px_0_rgba(255,255,255,0.8)]">
          <ChartContainer
            config={scoreRadarConfig}
            className="mx-auto h-[392px] w-full max-w-[560px]"
          >
            <RadarChart data={[...scoreRadarData]} outerRadius={136}>
              <ChartTooltip
                cursor={false}
                content={<ChartTooltipContent indicator="line" />}
              />
              <PolarGrid className="stroke-border/80" />
              <PolarAngleAxis
                dataKey="category"
                tick={{
                  fill: "var(--color-muted-foreground)",
                  fontSize: 11,
                }}
              />
              <RechartsRadar
                dataKey="average"
                fill="var(--color-average)"
                fillOpacity={0.08}
                stroke="var(--color-average)"
                strokeWidth={1.75}
              />
              <RechartsRadar
                dataKey="top5"
                fill="var(--color-top5)"
                fillOpacity={0.16}
                stroke="var(--color-top5)"
                strokeWidth={2.2}
              />
            </RadarChart>
          </ChartContainer>
          <div className="pointer-events-none absolute left-1/2 top-1/2 size-3 -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-white bg-primary shadow-[0_0_0_5px_rgba(37,99,235,0.14)]" />
        </div>
      </div>
    </SectionCard>
  )
}

function BusinessIntelligenceCard() {
  return (
    <SectionCard
      title="Business Intelligence"
      description="Prioritized recommendations based on your profile and the highest-impact growth opportunities."
      action={
        <Button variant="ghost" size="sm" className="rounded-full">
          View all
          <ArrowRight className="size-4" />
        </Button>
      }
    >
      <Table>
        <TableHeader>
          <TableRow className="border-border/80 hover:bg-transparent">
            <TableHead className="px-0 text-xs uppercase tracking-[0.16em] text-muted-foreground">
              Intelligence
            </TableHead>
            <TableHead className="text-xs uppercase tracking-[0.16em] text-muted-foreground">
              Value
            </TableHead>
            <TableHead className="pr-0 text-right text-xs uppercase tracking-[0.16em] text-muted-foreground">
              Recommended next
            </TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {intelligenceRows.map((row) => (
            <TableRow key={row.name} className="border-border/70">
              <TableCell className="px-0 py-4">
                <div className="flex items-center gap-3">
                  <div className="grid size-9 place-items-center rounded-full bg-white text-primary shadow-[0_1px_0_rgba(15,23,42,0.04)]">
                    <Sparkles className="size-4 stroke-[1.9]" />
                  </div>
                  <div>
                    <p className="font-medium text-foreground">{row.name}</p>
                    <p className="text-xs text-muted-foreground">
                      Opportunity signal
                    </p>
                  </div>
                </div>
              </TableCell>
              <TableCell className="py-4 text-sm font-semibold text-foreground">
                {row.value}
              </TableCell>
              <TableCell className="py-4 pr-0 text-right">
                  <Badge
                    variant="outline"
                    className="rounded-full border-emerald-200/80 bg-white px-2.5 py-1 text-[11px] text-emerald-700"
                  >
                    {row.impact}
                  </Badge>
                </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </SectionCard>
  )
}

function FocusAreasCard() {
  return (
    <SectionCard
      title="Your Focus Areas"
      description="As you complete more of your journey, Point93 will consolidate the most important actions here."
      className="min-h-[332px]"
    >
      <div className="flex h-full min-h-[220px] flex-col justify-between rounded-[16px] bg-white p-5">
        <div className="grid size-11 place-items-center rounded-full bg-muted text-primary">
          <Workflow className="size-5 stroke-[1.9]" />
        </div>
        <div className="space-y-2">
          <p className="text-[15px] font-medium tracking-[-0.015em] text-foreground">
            No focus areas yet
          </p>
          <p className="text-sm leading-6 text-muted-foreground">
            Finish your first module to generate tailored focus areas and see
            how your priorities should stack over time.
          </p>
        </div>
        <Button variant="outline" className="w-fit rounded-full">
          Review the journey
        </Button>
      </div>
    </SectionCard>
  )
}

function DashboardRightRail({
  collapsed,
}: {
  collapsed: boolean
}) {
  if (collapsed) {
    return null
  }

  return (
    <>
      <div className="mt-6 space-y-4 xl:hidden">
        <RightRailContent />
      </div>
      <aside className="hidden xl:block">
        <div
          className="fixed inset-y-0 right-0 overflow-y-auto border-l border-border/80 bg-sidebar"
          style={{ width: `${RIGHT_RAIL_WIDTH}px` }}
        >
          <div className="flex min-h-full flex-col">
            <RightRailContent />
          </div>
        </div>
      </aside>
    </>
  )
}

function RightRailContent() {
  return (
    <div className="pt-[88px]">
      <ProfileScoreCard />
      <RightRailSection
        title="Intelligence Profiles"
        action={
          <Button
            variant="secondary"
            size="sm"
            className="px-3"
          >
            View all
          </Button>
        }
      >
        <div className={cn(RIGHT_RAIL_STAGE_CLASS, "space-y-4")}>
          {profileRows.map((row) => (
            <div key={row.name} className="space-y-2">
              <div className="flex items-center justify-between gap-3 text-sm">
                <div className="flex items-center gap-2">
                  <div className="grid size-7 place-items-center rounded-full bg-white text-primary shadow-[0_1px_0_rgba(15,23,42,0.04)]">
                    <Star className="size-3.5 stroke-[1.8]" />
                  </div>
                  <span className="font-medium text-foreground">
                    {row.name}
                  </span>
                </div>
                <span className="text-muted-foreground">{row.value}%</span>
              </div>
              <div className="h-2 rounded-full bg-white">
                <div
                  className="h-full rounded-full bg-primary/70"
                  style={{ width: `${row.value}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      </RightRailSection>
      <RightRailSection
        title="What Clients Are Asking"
        action={
          <Badge
            variant="outline"
            className="rounded-full border-border bg-white px-2.5 py-1 text-[11px]"
          >
            Coming soon
          </Badge>
        }
      >
        <div className={cn(RIGHT_RAIL_STAGE_CLASS, "space-y-4")}>
          <div className="rounded-[16px] bg-white/92 p-4 shadow-[inset_0_1px_0_rgba(255,255,255,0.9)]">
            <p className="text-sm leading-6 text-muted-foreground">
              “Should I be worried about the fee changes?”
            </p>
          </div>
          <div className="space-y-2 text-sm">
            <div className="flex items-center justify-between gap-3">
              <span className="text-muted-foreground">Advisors ready</span>
              <span className="font-medium text-foreground">66%</span>
            </div>
            <div className="flex items-center justify-between gap-3">
              <span className="text-muted-foreground">Your readiness</span>
              <span className="font-medium text-foreground">72%</span>
            </div>
          </div>
          <Button className="w-full rounded-full">Improve your ranking</Button>
        </div>
      </RightRailSection>
      <RightRailSection
        title="Insight Areas"
        description="Complete modules to reveal the insight areas most relevant to your business."
      >
        <div
          className={cn(
            RIGHT_RAIL_STAGE_CLASS,
            "text-sm leading-6 text-muted-foreground"
          )}
        >
          Your strongest and weakest operating areas will appear here once
          enough assessment data has been collected.
        </div>
      </RightRailSection>
    </div>
  )
}

function ProfileScoreCard() {
  return (
    <section className="border-b border-border/75 px-5 pb-5 pt-4">
      <div className="flex flex-col items-center">
        <div className="relative h-[104px] w-[164px]">
          <svg
            width="164"
            height="104"
            viewBox="0 0 164 104"
            className="overflow-visible"
            aria-hidden="true"
          >
            <path
              d="M 6 82 A 70 70 0 0 1 146 82"
              fill="none"
              stroke="rgba(148,163,184,0.24)"
              strokeWidth="12"
              strokeLinecap="round"
            />
          </svg>
          <div className="absolute inset-x-0 top-10 text-center">
            <p className="font-[family:var(--font-display)] text-[2.44rem] leading-none font-normal tracking-[-0.03em] text-foreground">
              0
            </p>
            <p className="mt-1 text-[12px] text-muted-foreground">
              Advisor Score
            </p>
            <Badge
              variant="outline"
              className="mt-2 rounded-full border-border bg-muted px-2.5 py-0.5 text-[11px] font-medium text-muted-foreground"
            >
              Not Started
            </Badge>
          </div>
        </div>
      </div>
      <div className="my-4 border-t border-border/70" />
      <div>
        <p className="mb-2 text-[12px] text-muted-foreground">
          Profile Completion
        </p>
        <div className="mb-2 h-2 overflow-hidden rounded-full bg-muted">
          <div className="h-full w-0 rounded-full bg-muted-foreground/55 transition-all duration-500" />
        </div>
        <p className="text-[12px] text-foreground">
          <span className="font-medium">0 of 18</span> modules · Comprehensive
        </p>
      </div>
    </section>
  )
}

function RightRailSection({
  title,
  description,
  action,
  children,
}: {
  title: string
  description?: string
  action?: React.ReactNode
  children: React.ReactNode
}) {
  return (
    <section className="border-b border-border/75 px-5 py-5 last:border-b-0">
      <div className="flex items-start justify-between gap-3">
        <div className="space-y-1">
          <h2 className="text-[14px] font-medium tracking-[-0.015em] text-foreground">
            {title}
          </h2>
          {description ? (
            <p className="text-[12px] leading-[1.55] text-muted-foreground">
              {description}
            </p>
          ) : null}
        </div>
        {action ? <div className="shrink-0">{action}</div> : null}
      </div>
      <div className="mt-5">{children}</div>
    </section>
  )
}
