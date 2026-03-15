import * as React from "react"
import {
  ArrowRight,
  BarChart3,
  Bell,
  BookOpenText,
  ChevronLeft,
  ChevronRight,
  Gauge,
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

const metricCards = [
  { icon: Gauge, value: "0", label: "Overall Score" },
  { icon: BarChart3, value: "Pending", label: "Performance" },
  { icon: Trophy, value: "Top 5%", label: "Go to Top 5%" },
  { icon: Target, value: "Average", label: "Go to Average" },
  { icon: BookOpenText, value: "0 / 18", label: "Modules Completed" },
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
    title: "Module Level Scorecard",
    body: "Complete modules to see scorecard detail and benchmark placement.",
  },
  {
    title: "Module Performance Board",
    body: "Complete modules to see performance signals and trend movement.",
  },
  {
    title: "Data Point Scores",
    body: "Complete modules to see your scored data points and recommendations.",
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
      <div className="min-h-svh bg-[radial-gradient(circle_at_top,_rgba(255,255,255,0.96),_rgba(241,246,255,0.92)_48%,_rgba(236,241,248,0.88)_100%)]">
        <header className="sticky top-0 z-20 border-b border-border/75 bg-background/82 backdrop-blur-xl">
          <div className="mx-auto flex max-w-[1500px] items-center justify-between gap-4 px-5 py-4 sm:px-8">
            <div className="flex items-center gap-3">
              <SidebarTrigger
                variant="outline"
                size="icon-sm"
                className="rounded-full md:hidden"
              />
              <div>
                <p className="text-xs font-medium tracking-[0.16em] text-muted-foreground uppercase">
                  Point93 advisory dashboard
                </p>
                <h1 className="text-[1.9rem] font-semibold tracking-[-0.03em] text-foreground">
                  Welcome back, Adam
                </h1>
              </div>
            </div>
            <div className="flex items-center gap-3">
              <Badge
                variant="outline"
                className="hidden rounded-full border-border/80 bg-white/70 px-3 py-1 text-[11px] text-muted-foreground md:inline-flex"
              >
                Comprehensive
              </Badge>
              <Button variant="outline" size="sm" className="rounded-full">
                <Bell className="size-4" />
                Live Feedback
              </Button>
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
          rightRailWidth={rightRailCollapsed ? 0 : 320}
        />

        <main className="mx-auto max-w-[1500px] px-5 py-6 sm:px-8 sm:py-8">
          <div
            className={
              rightRailCollapsed
                ? "grid gap-0 xl:grid-cols-[minmax(0,1fr)_0rem]"
                : "grid gap-6 xl:grid-cols-[minmax(0,1fr)_20rem]"
            }
          >
            <div className="space-y-6">
              <SectionCard
                title="Start Your Assessment"
                description="Complete your first module to unlock scores, comparisons, and targeted business-intelligence recommendations."
                action={
                  <Badge className="rounded-full bg-primary/10 px-3 py-1 text-[11px] font-medium text-primary">
                    Current plan
                  </Badge>
                }
                className="overflow-hidden rounded-[18px] border-border/70 bg-[linear-gradient(135deg,rgba(252,254,255,0.98),rgba(232,241,255,0.9))]"
              >
                <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
                  <div className="max-w-2xl space-y-3">
                    <p className="text-sm leading-6 text-muted-foreground">
                      Your priority modules will appear here based on what
                      actually wins and keeps clients.
                    </p>
                    <div className="flex flex-wrap gap-2">
                      <Badge
                        variant="outline"
                        className="rounded-full border-primary/12 bg-white/80 px-2.5 py-1 text-[11px] text-foreground/72"
                      >
                        18 modules in journey
                      </Badge>
                      <Badge
                        variant="outline"
                        className="rounded-full border-primary/12 bg-white/80 px-2.5 py-1 text-[11px] text-foreground/72"
                      >
                        Personalized by plan
                      </Badge>
                    </div>
                  </div>
                  <Button size="lg" className="rounded-full px-5">
                    Begin First Module
                    <ArrowRight className="size-4" />
                  </Button>
                </div>
              </SectionCard>

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
                      className="min-h-[180px]"
                      contentClassName="flex h-full items-start"
                    >
                      <p className="text-sm leading-6 text-muted-foreground">
                        {card.body}
                      </p>
                    </SectionCard>
                  ))}
                </div>
              </section>

              <SectionCard
                title="Strengths / Weaknesses"
                description="Complete modules to see your strengths and areas needing attention."
              >
                <div className="rounded-[20px] border border-dashed border-border bg-muted/35 px-5 py-8 text-sm leading-6 text-muted-foreground">
                  Your first assessment will unlock a clearer read on what is
                  already working well and what should change next.
                </div>
              </SectionCard>

              <section className="grid gap-6 xl:grid-cols-[minmax(0,1.25fr)_minmax(0,0.9fr)]">
                <BusinessIntelligenceCard />
                <FocusAreasCard />
              </section>
            </div>

            <DashboardRightRail
              collapsed={rightRailCollapsed}
            />
          </div>
        </main>
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
          ? "fixed top-1/2 z-30 hidden h-12 w-6 -translate-y-1/2 rounded-r-md rounded-l-none border-slate-300 bg-white text-slate-600 shadow-md md:flex"
          : "fixed top-1/2 z-30 hidden h-12 w-6 -translate-y-1/2 rounded-l-md rounded-r-none border-slate-300 bg-white text-slate-600 shadow-md xl:flex"
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
              right:
                rightRailWidth === 0
                  ? "max(calc((100vw - 1500px) / 2), 0px)"
                  : `max(calc((100vw - 1500px) / 2 + ${rightRailWidth}px), ${rightRailWidth}px)`,
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
      title="Score Summary"
      description="Complete assessments to see your score plotted against top-performing advisors and the broader industry."
      className="min-h-[460px]"
    >
      <div className="space-y-5">
        <div className="flex flex-wrap gap-2">
          <Badge
            variant="outline"
            className="rounded-full border-[color:var(--chart-1)]/25 bg-[color:var(--chart-1)]/8 px-3 py-1 text-[11px] text-[color:var(--chart-1)]"
          >
            Your score vs top 5%
          </Badge>
          <Badge
            variant="outline"
            className="rounded-full border-[color:var(--chart-2)]/25 bg-[color:var(--chart-2)]/8 px-3 py-1 text-[11px] text-[color:var(--chart-2)]"
          >
            Industry average
          </Badge>
        </div>
        <ChartContainer
          config={scoreRadarConfig}
          className="mx-auto h-[372px] w-full max-w-[540px]"
        >
          <RadarChart data={[...scoreRadarData]} outerRadius={132}>
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
        <p className="text-center text-sm leading-6 text-muted-foreground">
          Complete assessments to calculate your personal score and see where
          your current business model stands today.
        </p>
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
                  <div className="grid size-9 place-items-center rounded-full bg-primary/8 text-primary">
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
                  className="rounded-full border-emerald-200 bg-emerald-50 px-2.5 py-1 text-[11px] text-emerald-700"
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
      <div className="flex h-full min-h-[220px] flex-col justify-between rounded-[22px] bg-muted/35 p-5">
        <div className="grid size-11 place-items-center rounded-full bg-primary/8 text-primary">
          <Workflow className="size-5 stroke-[1.9]" />
        </div>
        <div className="space-y-2">
          <p className="text-base font-semibold tracking-[-0.02em] text-foreground">
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
  return (
    <aside className="relative xl:sticky xl:top-[92px] xl:self-start">
      {collapsed ? (
        <div aria-hidden="true" className="min-h-[720px]" />
      ) : (
        <div className="space-y-4">
          <ProfileScoreCard />
          <SectionCard
            title="Intelligence Profiles"
            action={
              <Button variant="ghost" size="sm" className="rounded-full">
                View all
              </Button>
            }
          >
            <div className="space-y-4">
              {profileRows.map((row) => (
                <div key={row.name} className="space-y-2">
                  <div className="flex items-center justify-between gap-3 text-sm">
                    <div className="flex items-center gap-2">
                      <div className="grid size-7 place-items-center rounded-full bg-amber-100 text-amber-700">
                        <Star className="size-3.5 stroke-[1.8]" />
                      </div>
                      <span className="font-medium text-foreground">
                        {row.name}
                      </span>
                    </div>
                    <span className="text-muted-foreground">{row.value}%</span>
                  </div>
                  <div className="h-2 rounded-full bg-muted">
                    <div
                      className="h-full rounded-full bg-primary/70"
                      style={{ width: `${row.value}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </SectionCard>
          <SectionCard
            title="What Clients Are Asking"
            action={
              <Badge
                variant="outline"
                className="rounded-full border-border/80 bg-muted/50 px-2.5 py-1 text-[11px]"
              >
                Coming soon
              </Badge>
            }
          >
            <div className="space-y-4">
              <div className="rounded-[20px] bg-muted/45 p-4">
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
              <Button className="w-full rounded-full">
                Improve your ranking
              </Button>
            </div>
          </SectionCard>
          <SectionCard
            title="Insight Areas"
            description="Complete modules to reveal the insight areas most relevant to your business."
          >
            <div className="rounded-[20px] border border-dashed border-border bg-muted/35 p-4 text-sm leading-6 text-muted-foreground">
              Your strongest and weakest operating areas will appear here once
              enough assessment data has been collected.
            </div>
          </SectionCard>
        </div>
      )}
    </aside>
  )
}

function ProfileScoreCard() {
  return (
    <div className="rounded-[18px] border border-border/70 bg-card/96 p-5 shadow-[0_18px_34px_-32px_rgba(15,23,42,0.18)]">
      <div className="flex flex-col items-center">
        <div className="relative h-[92px] w-[164px]">
          <svg
            width="164"
            height="92"
            viewBox="0 0 164 92"
            className="overflow-visible"
            aria-hidden="true"
          >
            <path
              d="M 6 76 A 70 70 0 0 1 146 76"
              fill="none"
              stroke="rgba(148,163,184,0.24)"
              strokeWidth="12"
              strokeLinecap="round"
            />
          </svg>
          <div className="absolute inset-x-0 top-8 text-center">
            <p className="text-[2.5rem] leading-none font-semibold tracking-[-0.05em] text-foreground">
              0
            </p>
            <p className="mt-1 text-[12px] text-muted-foreground">
              Advisor Score
            </p>
            <Badge
              variant="outline"
              className="mt-2 rounded-full border-slate-200 bg-slate-100 px-2.5 py-0.5 text-[11px] font-medium text-slate-600"
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
          <div className="h-full w-0 rounded-full bg-slate-400 transition-all duration-500" />
        </div>
        <p className="text-[12px] text-foreground">
          <span className="font-semibold">0 of 18</span> modules · Comprehensive
        </p>
      </div>
    </div>
  )
}
