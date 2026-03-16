import * as React from "react"
import {
  ArrowRight,
  BarChart3,
  BookOpenText,
  ChevronLeft,
  ChevronRight,
  CircleHelp,
  Gauge,
  MessageSquare,
  Sparkles,
  Star,
  Target,
  Trophy,
  Workflow,
  type LucideIcon,
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
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
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
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
import { cn } from "@/lib/utils"

const RIGHT_RAIL_WIDTH = 340
const RIGHT_RAIL_STAGE_CLASS =
  "rounded-[18px] border border-border/75 bg-[linear-gradient(180deg,rgba(245,248,252,0.98),rgba(250,252,254,1))] px-4 py-4 shadow-[inset_0_1px_0_rgba(255,255,255,0.8)]"

export type DashboardScenario = "zero" | "partial" | "active"

type DashboardMetricCard = {
  icon: LucideIcon
  value: string
  label: string
  tooltip: string
  sparkline?: readonly number[]
}

type ScoreRadarDatum = {
  category: string
  top5: number
  average: number
  you: number
}

type HeroScenario = {
  title: string
  body: string
  cta: string
  animateCta?: boolean
}

type StrengthsScenario = {
  empty: boolean
  strengths?: readonly string[]
  gaps?: readonly string[]
}

type ModuleCardScenario = {
  title: string
  tooltip: string
  state: "empty" | "filled"
  items?: readonly {
    label: string
    value: string
    tone?: "positive" | "neutral" | "caution"
  }[]
}

type IntelligenceRow = {
  name: string
  value: string
  impact: string
}

type ProfileRow = {
  name: string
  value: number
  tooltip: string
}

type FocusAreaItem = {
  title: string
  note: string
}

type InsightAreaItem = {
  name: string
  score: string
  note: string
}

type DashboardScenarioData = {
  hero: HeroScenario
  metricCards: readonly DashboardMetricCard[]
  scoreSummary: {
    subtitle: string
    data: readonly ScoreRadarDatum[]
    showYouShape: boolean
  }
  strengths: StrengthsScenario
  moduleCards: readonly ModuleCardScenario[]
  intelligenceRows: readonly IntelligenceRow[]
  focusAreas: {
    empty: boolean
    items?: readonly FocusAreaItem[]
  }
  rightRail: {
    advisorScore: number
    scoreStatus: string
    modulesCompleted: number
    totalModules: number
    profileRows: readonly ProfileRow[]
    insightAreas?: readonly InsightAreaItem[]
  }
}

const moduleCardDefinitions = [
  {
    title: "Level Scorecard",
    tooltip: "Shows module scorecard detail and benchmark placement.",
  },
  {
    title: "Performance",
    tooltip: "Shows performance signals and trend movement by module.",
  },
  {
    title: "Datapoint Scoring",
    tooltip: "Shows scored data points and recommendations behind each module.",
  },
] as const

const dashboardScenarios: Record<DashboardScenario, DashboardScenarioData> = {
  zero: {
    hero: {
      title: "Start Your Assessment",
      body: "Complete the first module to see your scores and priorities.",
      cta: "Begin First Module",
      animateCta: true,
    },
    metricCards: [
      {
        icon: Gauge,
        value: "0",
        label: "Overall Score",
        tooltip: "Overall score, band, and percentile across completed modules.",
      },
      {
        icon: BarChart3,
        value: "—",
        label: "Performance",
        tooltip: "Your ranking relative to peers across completed modules.",
      },
      {
        icon: Trophy,
        value: "—",
        label: "Gap to Top 5%",
        tooltip: "Distance between your current score and top-performing advisors.",
      },
      {
        icon: Target,
        value: "—",
        label: "Gap to Average",
        tooltip: "Distance between your current score and the industry average.",
      },
      {
        icon: BookOpenText,
        value: "0/18",
        label: "Modules Completed",
        tooltip: "Completed modules unlock deeper scores, insights, and BI access.",
      },
    ],
    scoreSummary: {
      subtitle: "Complete modules to see your top growth areas.",
      showYouShape: false,
      data: [
        { category: "Professional", top5: 72, average: 38, you: 0 },
        { category: "Fees", top5: 61, average: 33, you: 0 },
        { category: "Client Service", top5: 78, average: 47, you: 0 },
        { category: "Planning", top5: 67, average: 35, you: 0 },
        { category: "Investment", top5: 74, average: 42, you: 0 },
        { category: "Firm Platform", top5: 58, average: 31, you: 0 },
      ],
    },
    strengths: {
      empty: true,
    },
    moduleCards: moduleCardDefinitions.map((card) => ({
      ...card,
      state: "empty",
    })),
    intelligenceRows: [
      { name: "NextGen Ready", value: "0", impact: "Highest impact" },
      { name: "Client Referrals", value: "0", impact: "High impact" },
      { name: "PitchPerfect", value: "0", impact: "High impact" },
      { name: "COI Referrals", value: "0", impact: "Highest impact" },
    ],
    focusAreas: {
      empty: true,
    },
    rightRail: {
      advisorScore: 0,
      scoreStatus: "Not Started",
      modulesCompleted: 0,
      totalModules: 18,
      profileRows: [
        {
          name: "NextGen Ready",
          value: 0,
          tooltip:
            "Strategic BI profile focused on multigenerational readiness and retention.",
        },
        {
          name: "Client Referrals",
          value: 0,
          tooltip:
            "Strategic BI profile focused on generating stronger referral momentum.",
        },
      ],
    },
  },
  partial: {
    hero: {
      title: "Recommended Next Module",
      body: "Continue with Fees, Value & Positioning to close one of your biggest score gaps.",
      cta: "Start Recommended Module",
    },
    metricCards: [
      {
        icon: Gauge,
        value: "41",
        label: "Overall Score",
        tooltip: "Overall score, band, and percentile across completed modules.",
        sparkline: [14, 16, 20, 24, 29, 34, 36, 39, 41],
      },
      {
        icon: BarChart3,
        value: "Top 46%",
        label: "Performance",
        tooltip: "Your ranking relative to peers across completed modules.",
        sparkline: [68, 64, 61, 58, 55, 52, 50, 48, 46],
      },
      {
        icon: Trophy,
        value: "19 pts",
        label: "Gap to Top 5%",
        tooltip: "Distance between your current score and top-performing advisors.",
        sparkline: [30, 28, 27, 25, 24, 22, 21, 20, 19],
      },
      {
        icon: Target,
        value: "6 pts",
        label: "Gap to Average",
        tooltip: "Distance between your current score and the industry average.",
        sparkline: [13, 12, 11, 10, 9, 8, 7, 7, 6],
      },
      {
        icon: BookOpenText,
        value: "4/18",
        label: "Modules Completed",
        tooltip: "Completed modules unlock deeper scores, insights, and BI access.",
      },
    ],
    scoreSummary: {
      subtitle: "Benchmark your current profile across the 6 core business areas.",
      showYouShape: true,
      data: [
        { category: "Professional", top5: 72, average: 38, you: 45 },
        { category: "Fees", top5: 61, average: 33, you: 34 },
        { category: "Client Service", top5: 78, average: 47, you: 51 },
        { category: "Planning", top5: 67, average: 35, you: 42 },
        { category: "Investment", top5: 74, average: 42, you: 40 },
        { category: "Firm Platform", top5: 58, average: 31, you: 36 },
      ],
    },
    strengths: {
      empty: false,
      strengths: [
        "Client service cadence is already above average.",
        "Planning conversations are becoming more consistent.",
      ],
      gaps: [
        "Fee articulation remains a drag on conversion.",
        "Platform confidence still trails stronger peers.",
      ],
    },
    moduleCards: [
      {
        ...moduleCardDefinitions[0],
        state: "filled",
        items: [
          { label: "Client Service", value: "58 · Competitive", tone: "positive" },
          { label: "Planning", value: "47 · Emerging", tone: "neutral" },
          { label: "Fees", value: "34 · At Risk", tone: "caution" },
        ],
      },
      {
        ...moduleCardDefinitions[1],
        state: "filled",
        items: [
          { label: "Client Service", value: "+6 vs last module", tone: "positive" },
          { label: "Planning", value: "+4 vs baseline", tone: "positive" },
          { label: "Fees", value: "-2 this month", tone: "caution" },
        ],
      },
      {
        ...moduleCardDefinitions[2],
        state: "filled",
        items: [
          { label: "Referral ask clarity", value: "72", tone: "positive" },
          { label: "Planning cadence", value: "64", tone: "neutral" },
          { label: "Fee positioning", value: "43", tone: "caution" },
        ],
      },
    ],
    intelligenceRows: [
      { name: "NextGen Ready", value: "41", impact: "Highest impact" },
      { name: "Client Referrals", value: "27", impact: "High impact" },
      { name: "PitchPerfect", value: "22", impact: "High impact" },
      { name: "COI Referrals", value: "18", impact: "Highest impact" },
    ],
    focusAreas: {
      empty: false,
      items: [
        {
          title: "Fee articulation",
          note: "Clarify value before pricing comes up.",
        },
        {
          title: "Next-gen engagement",
          note: "Start building visibility with heirs earlier.",
        },
        {
          title: "Referral capture",
          note: "Create a clearer post-review ask.",
        },
      ],
    },
    rightRail: {
      advisorScore: 41,
      scoreStatus: "Emerging",
      modulesCompleted: 4,
      totalModules: 18,
      profileRows: [
        {
          name: "NextGen Ready",
          value: 22,
          tooltip:
            "Strategic BI profile focused on multigenerational readiness and retention.",
        },
        {
          name: "Client Referrals",
          value: 14,
          tooltip:
            "Strategic BI profile focused on generating stronger referral momentum.",
        },
      ],
      insightAreas: [
        { name: "Client Service", score: "58", note: "Ahead of average" },
        { name: "Planning", score: "47", note: "Improving steadily" },
        { name: "Fees", score: "34", note: "Primary gap" },
      ],
    },
  },
  active: {
    hero: {
      title: "Recommended Next Module",
      body: "Complete Planning Process & Implementation to improve your score and sharpen your next growth priorities.",
      cta: "Start Recommended Module",
    },
    metricCards: [
      {
        icon: Gauge,
        value: "68",
        label: "Overall Score",
        tooltip: "Overall score, band, and percentile across completed modules.",
        sparkline: [42, 45, 47, 52, 56, 58, 61, 65, 68],
      },
      {
        icon: BarChart3,
        value: "Top 23%",
        label: "Performance",
        tooltip: "Your ranking relative to peers across completed modules.",
        sparkline: [31, 29, 28, 27, 26, 25, 24, 23, 23],
      },
      {
        icon: Trophy,
        value: "8 pts",
        label: "Gap to Top 5%",
        tooltip: "Distance between your current score and top-performing advisors.",
        sparkline: [18, 17, 16, 15, 14, 12, 11, 10, 8],
      },
      {
        icon: Target,
        value: "10 pts",
        label: "Gap to Average",
        tooltip: "Distance between your current score and the industry average.",
        sparkline: [22, 20, 18, 16, 15, 13, 12, 11, 10],
      },
      {
        icon: BookOpenText,
        value: "11/18",
        label: "Modules Completed",
        tooltip: "Completed modules unlock deeper scores, insights, and BI access.",
      },
    ],
    scoreSummary: {
      subtitle: "Benchmark your current profile across the 6 core business areas.",
      showYouShape: true,
      data: [
        { category: "Professional", top5: 72, average: 38, you: 58 },
        { category: "Fees", top5: 61, average: 33, you: 49 },
        { category: "Client Service", top5: 78, average: 47, you: 66 },
        { category: "Planning", top5: 67, average: 35, you: 62 },
        { category: "Investment", top5: 74, average: 42, you: 54 },
        { category: "Firm Platform", top5: 58, average: 31, you: 44 },
      ],
    },
    strengths: {
      empty: false,
      strengths: [
        "Client service and planning are already creating separation.",
        "Investment communication is outperforming the broader market.",
      ],
      gaps: [
        "Fee positioning is still the clearest unlock for the next jump.",
        "Firm platform confidence needs a stronger operating story.",
      ],
    },
    moduleCards: [
      {
        ...moduleCardDefinitions[0],
        state: "filled",
        items: [
          { label: "Client Service", value: "74 · Competitive", tone: "positive" },
          { label: "Planning", value: "69 · Competitive", tone: "positive" },
          { label: "Fees", value: "52 · Needs Work", tone: "caution" },
        ],
      },
      {
        ...moduleCardDefinitions[1],
        state: "filled",
        items: [
          { label: "Client Service", value: "+12 vs baseline", tone: "positive" },
          { label: "Planning", value: "+9 vs baseline", tone: "positive" },
          { label: "Firm Platform", value: "+5 vs last quarter", tone: "neutral" },
        ],
      },
      {
        ...moduleCardDefinitions[2],
        state: "filled",
        items: [
          { label: "Review follow-through", value: "81", tone: "positive" },
          { label: "Planning agenda clarity", value: "77", tone: "positive" },
          { label: "Fee framing consistency", value: "56", tone: "caution" },
        ],
      },
    ],
    intelligenceRows: [
      { name: "NextGen Ready", value: "63", impact: "Highest impact" },
      { name: "Client Referrals", value: "49", impact: "High impact" },
      { name: "PitchPerfect", value: "44", impact: "High impact" },
      { name: "COI Referrals", value: "37", impact: "Highest impact" },
    ],
    focusAreas: {
      empty: false,
      items: [
        {
          title: "Fee story refinement",
          note: "Translate value faster in the first 90 seconds.",
        },
        {
          title: "Next-gen relationship mapping",
          note: "Deepen visibility with heirs and spouses.",
        },
        {
          title: "Referral conversion",
          note: "Tighten the ask after moments of visible value.",
        },
      ],
    },
    rightRail: {
      advisorScore: 68,
      scoreStatus: "Competitive",
      modulesCompleted: 11,
      totalModules: 18,
      profileRows: [
        {
          name: "NextGen Ready",
          value: 61,
          tooltip:
            "Strategic BI profile focused on multigenerational readiness and retention.",
        },
        {
          name: "Client Referrals",
          value: 43,
          tooltip:
            "Strategic BI profile focused on generating stronger referral momentum.",
        },
      ],
      insightAreas: [
        { name: "Client Service", score: "74", note: "Strongest edge" },
        { name: "Planning", score: "69", note: "Above peer average" },
        { name: "Fees", score: "52", note: "Largest remaining gap" },
      ],
    },
  },
}

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

function InfoTooltip({
  label,
  children,
}: {
  label: string
  children: React.ReactNode
}) {
  return (
    <Tooltip>
      <TooltipTrigger
        render={
          <button
            type="button"
            aria-label={label}
            className="inline-flex size-5 items-center justify-center rounded-full opacity-60 transition-[opacity,color] hover:opacity-100 focus-visible:opacity-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring/60"
          />
        }
      >
        <CircleHelp className="size-3.5" />
      </TooltipTrigger>
      <TooltipContent
        side="top"
        align="start"
        className="max-w-[240px] text-[11px] leading-[1.45]"
      >
        {children}
      </TooltipContent>
    </Tooltip>
  )
}

const advisorScorePreviewPeak = 100

const clientQuestionFeed = [
  "Should I be worried about the fee changes?",
  "How do top advisors explain volatility without sounding reactive?",
  "What should I say when clients ask if rates will fall again?",
  "How are firms reframing planning conversations this quarter?",
  "What are the best advisors saying about cash management right now?",
  "How should I answer clients asking whether to wait on the sidelines?",
  "What are firms doing to keep younger clients engaged?",
  "How are advisors handling the shift toward more planning-led conversations?",
  "What are clients asking about private markets this month?",
  "How do top teams talk about downside protection without sounding defensive?",
  "What are advisors saying when clients ask about rebalancing?",
  "How should I position my value when clients focus on fees?",
  "How are leading advisors talking about tax-aware positioning this year?",
  "What should I say when clients ask if they should keep excess cash parked?",
  "How are top firms framing estate planning conversations right now?",
  "What are advisors hearing from clients who want more downside protection?",
  "How should I respond when clients compare me to low-cost digital offerings?",
  "What are advisors saying when business-owner clients ask about succession?",
] as const

export function Point93DashboardPage({
  scenario = "zero",
}: {
  scenario?: DashboardScenario
}) {
  return (
    <SidebarProvider defaultOpen>
      <AppSidebar />
      <DashboardShell scenario={scenario} />
    </SidebarProvider>
  )
}

function DashboardShell({
  scenario,
}: {
  scenario: DashboardScenario
}) {
  const [rightRailCollapsed, setRightRailCollapsed] = React.useState(false)
  const { state, toggleSidebar } = useSidebar()
  const leftSidebarCollapsed = state === "collapsed"
  const scenarioData = dashboardScenarios[scenario]

  return (
    <SidebarInset className="bg-transparent">
      <div className="min-h-svh bg-background">
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
            "relative overflow-hidden px-5 pb-8 pt-0 sm:px-8 sm:pb-10",
            !rightRailCollapsed && "xl:pr-[23rem]"
          )}
        >
          <div className="pointer-events-none absolute inset-x-0 top-0 h-[332px] bg-[linear-gradient(180deg,#0d2f78_0%,#17429d_100%)]" />
          <div className="pointer-events-none absolute inset-x-0 bottom-0 top-[332px] bg-[linear-gradient(180deg,#fbfcfe_0%,#f6f8fb_58%,#f8f5f1_100%)]" />
          <div className="relative z-10 mx-auto max-w-[1120px]">
            <section className="pb-14 pt-9 text-white sm:pb-20 sm:pt-10">
              <div className="flex items-center gap-3">
                <SidebarTrigger
                  variant="outline"
                  size="icon-sm"
                  className="rounded-full border-white/18 bg-white/10 text-white hover:bg-white/14 hover:text-white md:hidden"
                />
                <div>
                  <h1 className="font-[family:var(--font-brand)] text-[1rem] leading-[1.06] font-normal tracking-[-0.03em] text-white sm:text-[1.125rem]">
                    Welcome back, Brendon
                  </h1>
                </div>
              </div>

              <div className="mt-6 h-px w-full bg-white/16" />

              <div className="mt-7 flex flex-col gap-5 md:flex-row md:items-start md:justify-between md:gap-8">
                <div className="max-w-2xl">
                  <h2 className="font-[family:var(--font-brand)] text-[1.38rem] leading-[1.06] font-medium tracking-[-0.03em] text-white sm:text-[1.55rem]">
                    {scenarioData.hero.title}
                  </h2>
                  <p className="mt-3 max-w-[35rem] text-[15px] leading-[1.6] text-white/82 sm:text-[16px]">
                    {scenarioData.hero.body}
                  </p>
                </div>
                <Button
                  size="lg"
                  className={cn(
                    "h-11 shrink-0 self-start rounded-full bg-white px-7 text-[0.95rem] font-medium text-primary hover:bg-white/96",
                    scenarioData.hero.animateCta && "cta-breathe"
                  )}
                >
                  {scenarioData.hero.cta}
                  <ArrowRight className="size-4" />
                </Button>
              </div>
            </section>

            <div className="-mt-12 rounded-[28px] border border-border/80 bg-white p-5 shadow-[0_28px_60px_-38px_rgba(15,23,42,0.24)] sm:-mt-14 sm:p-6">
              <div className="space-y-6">
                <section className="grid gap-4 lg:grid-cols-2 2xl:grid-cols-5">
                  {scenarioData.metricCards.map((card) => (
                    <MetricCard key={card.label} {...card} />
                  ))}
                </section>

                <section className="grid gap-6 xl:grid-cols-[minmax(0,1fr)_320px]">
                  <div className="grid gap-4">
                    <ScoreSummaryCard data={scenarioData.scoreSummary} />
                    <StrengthsWeaknessesCard data={scenarioData.strengths} />
                  </div>
                  <div className="grid gap-4 xl:grid-cols-1">
                    {scenarioData.moduleCards.map((card) => (
                      <SectionCard
                        key={card.title}
                        title={card.title}
                        titleAccessory={
                          <InfoTooltip label={`About ${card.title}`}>
                            {card.tooltip}
                          </InfoTooltip>
                        }
                        surface="outlined"
                        compactHeader
                        className="min-h-[180px]"
                        contentClassName="flex h-full items-center justify-center"
                      >
                        {card.state === "empty" ? (
                          <div className="flex w-full flex-col items-center justify-center gap-4 py-1">
                            <div className="grid size-12 place-items-center rounded-full bg-muted text-muted-foreground/75">
                              <BookOpenText className="size-5 stroke-[1.7]" />
                            </div>
                            <Button
                              variant="outline"
                              size="default"
                              className="h-9 rounded-[6px] border-border/90 bg-white px-4 text-[0.82rem] shadow-none hover:bg-muted/45"
                            >
                              Start First Module
                            </Button>
                          </div>
                        ) : (
                          <div className="w-full space-y-3 py-1">
                            {card.items?.map((item) => (
                              <div
                                key={`${card.title}-${item.label}`}
                                className="flex items-center justify-between border-b border-border/65 pb-2 last:border-b-0 last:pb-0"
                              >
                                <span className="text-[12.5px] text-muted-foreground">
                                  {item.label}
                                </span>
                                <span
                                  className={cn(
                                    "text-[12.5px] font-medium",
                                    item.tone === "positive"
                                      ? "text-emerald-700"
                                      : item.tone === "caution"
                                        ? "text-amber-700"
                                        : "text-foreground"
                                  )}
                                >
                                  {item.value}
                                </span>
                              </div>
                            ))}
                          </div>
                        )}
                      </SectionCard>
                    ))}
                  </div>
                </section>

                <section className="grid gap-6 xl:grid-cols-[minmax(0,1.25fr)_minmax(0,0.9fr)]">
                  <BusinessIntelligenceCard rows={scenarioData.intelligenceRows} />
                  <FocusAreasCard data={scenarioData.focusAreas} />
                </section>
              </div>
            </div>
          </div>
          <DashboardRightRail
            collapsed={rightRailCollapsed}
            data={scenarioData.rightRail}
          />
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
              left: collapsed ? "3.5rem" : "16rem",
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
              

function ScoreSummaryCard({
  data,
}: {
  data: DashboardScenarioData["scoreSummary"]
}) {
  return (
    <Card className="min-h-[344px] rounded-[16px] border border-[#223a61] bg-[linear-gradient(180deg,#263d68_0%,#203457_100%)] text-white shadow-[0_18px_42px_-30px_rgba(15,23,42,0.55)] ring-0">
      <CardHeader className="grid grid-cols-[1fr_auto] items-start gap-3 px-5 pb-0 pt-4">
        <div className="space-y-1.5">
          <div className="flex items-center gap-2">
            <CardTitle className="font-[family:var(--font-brand)] text-[22px] leading-[1.08] font-semibold tracking-[-0.04em] text-white">
              How You Compare
            </CardTitle>
            <InfoTooltip label="About How You Compare">
              Compare your current score profile to top-performing advisors and
              the industry average across core business areas.
            </InfoTooltip>
          </div>
          <p className="text-[13px] leading-[1.45] text-white/66">
            {data.subtitle}
          </p>
        </div>
        <div className="flex flex-wrap items-center justify-end gap-x-4 gap-y-1 text-[11px] text-white/72">
          <div className="flex items-center gap-2">
            <span className="size-2.5 rounded-full bg-primary shadow-[0_0_0_3px_rgba(37,99,235,0.16)]" />
            <span>You</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="size-2.5 rounded-full bg-[#fb923c]" />
            <span>Top 5%</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="block w-4 border-t-2 border-dashed border-[#2dd4bf]" />
            <span>Industry average</span>
          </div>
        </div>
      </CardHeader>
      <CardContent className="px-4 pb-1 pt-1">
        <div className="relative">
          <ChartContainer
            config={scoreRadarConfig}
            className="mx-auto h-[286px] w-full max-w-[500px] [&_.recharts-polar-grid_[stroke='#ccc']]:stroke-white/14 [&_.recharts-text]:fill-white/58"
          >
            <RadarChart
              data={[...data.data]}
              outerRadius={114}
              margin={{ top: 18, right: 38, bottom: 0, left: 38 }}
            >
              <ChartTooltip
                cursor={false}
                content={<ChartTooltipContent indicator="line" />}
              />
              <PolarGrid className="stroke-white/14" />
              <PolarAngleAxis
                dataKey="category"
                tick={{
                  fill: "rgba(255,255,255,0.58)",
                  fontSize: 12.5,
                }}
              />
              {data.showYouShape ? (
                <RechartsRadar
                  dataKey="you"
                  fill="rgba(37,99,235,0.18)"
                  stroke="rgba(96,165,250,0.98)"
                  strokeWidth={2}
                />
              ) : null}
              <RechartsRadar
                dataKey="average"
                fill="rgba(45,212,191,0.06)"
                stroke="rgba(45,212,191,0.92)"
                strokeWidth={1.5}
                strokeDasharray="4 5"
              />
              <RechartsRadar
                dataKey="top5"
                fill="rgba(251,146,60,0.14)"
                stroke="rgba(251,146,60,0.96)"
                strokeWidth={2}
              />
            </RadarChart>
          </ChartContainer>
          {!data.showYouShape ? (
            <div className="pointer-events-none absolute left-1/2 top-1/2 size-3 -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-[#203457] bg-primary shadow-[0_0_0_5px_rgba(37,99,235,0.16)]" />
          ) : null}
        </div>
      </CardContent>
    </Card>
  )
}

function StrengthsWeaknessesCard({
  data,
}: {
  data: DashboardScenarioData["strengths"]
}) {
  return (
    <SectionCard
      title="Strengths / Weaknesses"
      titleAccessory={
        <InfoTooltip label="About Strengths / Weaknesses">
          Edge and exposure ranking surfaces your top strengths and growth
          areas.
        </InfoTooltip>
      }
      description="Complete modules to see your strengths and areas needing attention."
      className="min-h-[152px]"
      contentClassName="pt-[10px]"
    >
      {data.empty ? (
        <div className="rounded-[14px] bg-white px-4 py-5 text-sm leading-6 text-muted-foreground">
          Your first assessment will unlock a clearer read on what is already
          working well and what should change next.
        </div>
      ) : (
        <div className="grid gap-4 rounded-[14px] bg-white px-4 py-4 md:grid-cols-2">
          <div className="space-y-2">
            <p className="text-[11px] font-medium uppercase tracking-[0.14em] text-muted-foreground">
              Strengths
            </p>
            <ul className="space-y-2 text-sm leading-5 text-foreground">
              {data.strengths?.map((item) => (
                <li key={item} className="flex gap-2">
                  <span className="mt-[0.42rem] size-1.5 shrink-0 rounded-full bg-emerald-500" />
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
          <div className="space-y-2">
            <p className="text-[11px] font-medium uppercase tracking-[0.14em] text-muted-foreground">
              Priority gaps
            </p>
            <ul className="space-y-2 text-sm leading-5 text-foreground">
              {data.gaps?.map((item) => (
                <li key={item} className="flex gap-2">
                  <span className="mt-[0.42rem] size-1.5 shrink-0 rounded-full bg-amber-500" />
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </SectionCard>
  )
}

function BusinessIntelligenceCard({
  rows,
}: {
  rows: readonly IntelligenceRow[]
}) {
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
          {rows.map((row) => (
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

function FocusAreasCard({
  data,
}: {
  data: DashboardScenarioData["focusAreas"]
}) {
  return (
    <SectionCard
      title="Your Focus Areas"
      description="As you complete more of your journey, Point93 will consolidate the most important actions here."
      className="min-h-[332px]"
    >
      {data.empty ? (
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
      ) : (
        <div className="rounded-[16px] bg-white px-5 py-4">
          <div className="space-y-3">
            {data.items?.map((item) => (
              <div
                key={item.title}
                className="border-b border-border/70 pb-3 last:border-b-0 last:pb-0"
              >
                <p className="text-[14px] font-medium tracking-[-0.015em] text-foreground">
                  {item.title}
                </p>
                <p className="mt-1 text-sm leading-5 text-muted-foreground">
                  {item.note}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </SectionCard>
  )
}

function DashboardRightRail({
  collapsed,
  data,
}: {
  collapsed: boolean
  data: DashboardScenarioData["rightRail"]
}) {
  if (collapsed) {
    return null
  }

  return (
    <>
      <div className="mt-6 space-y-4 xl:hidden">
        <RightRailContent data={data} />
      </div>
      <aside className="hidden xl:block">
        <div
          className="fixed inset-y-0 right-0 overflow-y-auto border-l border-border/80 bg-sidebar"
          style={{ width: `${RIGHT_RAIL_WIDTH}px` }}
        >
          <div className="flex min-h-full flex-col">
            <RightRailContent data={data} />
          </div>
        </div>
      </aside>
    </>
  )
}

function RightRailContent({
  data,
}: {
  data: DashboardScenarioData["rightRail"]
}) {
  return (
    <div className="pt-4">
      <ProfileScoreCard data={data} />
      <RightRailSection
        title="Intelligence Profiles"
        infoTooltip="Stage-based BI profiles surface strategic growth opportunities and can be unlocked through prerequisites or purchased directly."
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
          {data.profileRows.map((row) => (
            <div key={row.name} className="space-y-2">
              <div className="flex items-center justify-between gap-3 text-sm">
                <div className="flex items-center gap-2">
                  <div className="grid size-7 place-items-center rounded-full bg-white text-primary shadow-[0_1px_0_rgba(15,23,42,0.04)]">
                    <Star className="size-3.5 stroke-[1.8]" />
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="font-medium text-foreground">
                      {row.name}
                    </span>
                    <InfoTooltip label={`About ${row.name}`}>
                      {row.tooltip}
                    </InfoTooltip>
                  </div>
                </div>
                <span className="text-muted-foreground">{row.value}%</span>
              </div>
              <QuintileBar value={row.value} />
            </div>
          ))}
        </div>
      </RightRailSection>
      <RightRailSection
        title="What Clients Are Asking"
        infoTooltip="Periodic question sets on current industry topics, scored and benchmarked against the advisor community."
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
          <RotatingClientQuestionFeed />
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
        infoTooltip="Diagnostic themes ranked by gap priority; scores remain visible at every tier."
        description="Complete modules to reveal the insight areas most relevant to your business."
      >
        {data.insightAreas?.length ? (
          <div className={cn(RIGHT_RAIL_STAGE_CLASS, "space-y-3")}>
            {data.insightAreas.map((item) => (
              <div
                key={item.name}
                className="border-b border-border/65 pb-3 last:border-b-0 last:pb-0"
              >
                <div className="flex items-center justify-between gap-3">
                  <span className="text-sm font-medium text-foreground">
                    {item.name}
                  </span>
                  <span className="rounded-full bg-white px-2 py-0.5 text-[11px] font-medium text-foreground shadow-[0_1px_0_rgba(15,23,42,0.04)]">
                    {item.score}
                  </span>
                </div>
                <p className="mt-1 text-[12px] leading-[1.5] text-muted-foreground">
                  {item.note}
                </p>
              </div>
            ))}
          </div>
        ) : (
          <div
            className={cn(
              RIGHT_RAIL_STAGE_CLASS,
              "text-sm leading-6 text-muted-foreground"
            )}
          >
            Your strongest and weakest operating areas will appear here once
            enough assessment data has been collected.
          </div>
        )}
      </RightRailSection>
    </div>
  )
}

function QuintileBar({ value }: { value: number }) {
  const filledSegments = Math.max(0, Math.min(5, Math.ceil(value / 20)))

  return (
    <div className="grid grid-cols-5 gap-1">
      {Array.from({ length: 5 }, (_, index) => (
        <div
          key={index}
          className={cn(
            "h-2 rounded-full bg-white shadow-[inset_0_1px_0_rgba(255,255,255,0.85)]",
            index < filledSegments && "bg-primary/72"
          )}
        />
      ))}
    </div>
  )
}

function ProfileScoreCard({
  data,
}: {
  data: DashboardScenarioData["rightRail"]
}) {
  const [displayScore, setDisplayScore] = React.useState(data.advisorScore)
  const [displayDirection, setDisplayDirection] = React.useState<"up" | "down">(
    "up"
  )
  const previousScoreRef = React.useRef(data.advisorScore)

  React.useEffect(() => {
    const updateDisplayScore = (nextScore: number) => {
      if (nextScore === previousScoreRef.current) {
        return
      }

      setDisplayDirection(
        nextScore >= previousScoreRef.current ? "up" : "down"
      )
      previousScoreRef.current = nextScore
      setDisplayScore(nextScore)
    }

    if (data.advisorScore > 0) {
      updateDisplayScore(data.advisorScore)
      return
    }

    let frameId = 0
    let startTime: number | null = null

    const riseDuration = 1500
    const holdDuration = 650
    const fallDuration = 1050
    const totalDuration = riseDuration + holdDuration + fallDuration

    const animate = (timestamp: number) => {
      if (startTime === null) {
        startTime = timestamp
      }

      const elapsed = timestamp - startTime

      if (elapsed <= riseDuration) {
        const progress = elapsed / riseDuration
        updateDisplayScore(
          Math.round(advisorScorePreviewPeak * easeOutCubic(progress))
        )
      } else if (elapsed <= riseDuration + holdDuration) {
        updateDisplayScore(advisorScorePreviewPeak)
      } else if (elapsed <= totalDuration) {
        const progress = (elapsed - riseDuration - holdDuration) / fallDuration
        updateDisplayScore(
          Math.round(advisorScorePreviewPeak * (1 - easeInOutCubic(progress)))
        )
      } else {
        updateDisplayScore(0)
        return
      }

      frameId = window.requestAnimationFrame(animate)
    }

    frameId = window.requestAnimationFrame(animate)

    return () => window.cancelAnimationFrame(frameId)
  }, [data.advisorScore])

  const gaugeStroke = getAdvisorGaugeColor(displayScore)
  const completionPercent = Math.round(
    (data.modulesCompleted / data.totalModules) * 100
  )
  const gaugeStatus = data.scoreStatus
  const hasStarted = data.advisorScore > 0

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
            <path
              d="M 6 82 A 70 70 0 0 1 146 82"
              pathLength="100"
              fill="none"
              stroke={gaugeStroke}
              strokeWidth="12"
              strokeLinecap="round"
              strokeDasharray="100"
              strokeDashoffset={100 - displayScore}
            />
          </svg>
          <div className="absolute inset-x-0 top-10 text-center">
            <OdometerScore value={displayScore} direction={displayDirection} />
            <div className="mt-1 flex items-center justify-center gap-1.5 text-[12px] text-muted-foreground">
              <p>Advisor Score</p>
              <InfoTooltip label="About Advisor Score">
                Composite score and percentile summary across completed
                modules.
              </InfoTooltip>
            </div>
            <Badge
              variant="outline"
              className={cn(
                "mt-2 rounded-full px-2.5 py-0.5 text-[11px] font-medium",
                hasStarted
                  ? "border-blue-200 bg-blue-50 text-blue-700"
                  : "border-border bg-muted text-muted-foreground"
              )}
            >
              {gaugeStatus}
            </Badge>
          </div>
        </div>
      </div>
      <div className="my-4 border-t border-border/70" />
      <div>
        <div className="mb-2 flex items-center gap-1.5 text-[12px] text-muted-foreground">
          <p>Profile Completion</p>
          <InfoTooltip label="About Profile Completion">
            Tracks progress through the 18-module journey and unlocks deeper
            dashboard content over time.
          </InfoTooltip>
        </div>
        <div className="mb-2 h-2 overflow-hidden rounded-full bg-muted">
          <div
            className="h-full rounded-full bg-muted-foreground/55 transition-all duration-500"
            style={{ width: `${completionPercent}%` }}
          />
        </div>
        <p className="text-[12px] text-foreground">
          <span className="font-medium">
            {data.modulesCompleted} of {data.totalModules}
          </span>{" "}
          modules · Comprehensive
        </p>
      </div>
    </section>
  )
}

function OdometerScore({
  value,
  direction,
}: {
  value: number
  direction: "up" | "down"
}) {
  const digits = [
    {
      key: "hundreds",
      digit: Math.floor(value / 100) % 10,
      visible: value >= 100,
    },
    {
      key: "tens",
      digit: Math.floor(value / 10) % 10,
      visible: value >= 10,
    },
    {
      key: "ones",
      digit: value % 10,
      visible: true,
    },
  ] as const

  return (
    <div className="flex justify-center" aria-label={String(value)} role="text">
      <span className="sr-only">{value}</span>
      <div
        aria-hidden="true"
        className="inline-flex items-center justify-center font-[family:var(--font-display)] text-[2.44rem] leading-none font-normal tracking-[-0.03em] text-foreground"
      >
        {digits.map((digit) => (
          <OdometerDigit
            key={digit.key}
            digit={digit.digit}
            visible={digit.visible}
            direction={direction}
          />
        ))}
      </div>
    </div>
  )
}

function OdometerDigit({
  digit,
  visible,
  direction,
}: {
  digit: number
  visible: boolean
  direction: "up" | "down"
}) {
  const repeatCount = 30
  const centerOffset = 10
  const digitSequence = React.useMemo(
    () =>
      Array.from({ length: repeatCount * 10 }, (_, index) => index % 10),
    []
  )
  const [position, setPosition] = React.useState(centerOffset * 10 + digit)

  React.useEffect(() => {
    setPosition(centerOffset * 10 + digit)
  }, [])

  React.useEffect(() => {
    setPosition((current) => {
      let next = current

      if (direction === "up") {
        while (digitSequence[next % 10] !== digit) {
          next += 1
        }
      } else {
        while (digitSequence[((next % 10) + 10) % 10] !== digit) {
          next -= 1
        }
      }

      return next
    })
  }, [digit, digitSequence, direction])

  return (
    <div
      className={cn(
        "relative overflow-hidden transition-[width,opacity] duration-300 ease-out",
        visible ? "w-[0.68em] opacity-100" : "w-0 opacity-0"
      )}
      style={{ height: "1em" }}
    >
      <div
        className="absolute inset-x-0 top-0 transition-transform duration-300 ease-[cubic-bezier(0.22,1,0.36,1)]"
        style={{ transform: `translateY(-${position}em)` }}
      >
        {digitSequence.map((sequenceDigit, index) => (
          <div
            key={index}
            className="flex h-[1em] items-center justify-center"
            aria-hidden="true"
          >
            {sequenceDigit}
          </div>
        ))}
      </div>
    </div>
  )
}

function getAdvisorGaugeColor(score: number) {
  const clamped = Math.max(0, Math.min(100, score)) / 100
  return interpolateHexColor("#c7bbab", "#2563eb", clamped)
}

function interpolateHexColor(start: string, end: string, amount: number) {
  const from = hexToRgb(start)
  const to = hexToRgb(end)

  const red = Math.round(from[0] + (to[0] - from[0]) * amount)
  const green = Math.round(from[1] + (to[1] - from[1]) * amount)
  const blue = Math.round(from[2] + (to[2] - from[2]) * amount)

  return `rgb(${red}, ${green}, ${blue})`
}

function hexToRgb(value: string) {
  const normalized = value.replace("#", "")
  const safe =
    normalized.length === 3
      ? normalized
          .split("")
          .map((char) => char + char)
          .join("")
      : normalized

  return [
    parseInt(safe.slice(0, 2), 16),
    parseInt(safe.slice(2, 4), 16),
    parseInt(safe.slice(4, 6), 16),
  ] as const
}

function easeOutCubic(t: number) {
  return 1 - Math.pow(1 - t, 3)
}

function easeInOutCubic(t: number) {
  return t < 0.5
    ? 4 * t * t * t
    : 1 - Math.pow(-2 * t + 2, 3) / 2
}

function RotatingClientQuestionFeed() {
  const [activeIndex, setActiveIndex] = React.useState(0)
  const [isAnimating, setIsAnimating] = React.useState(false)

  React.useEffect(() => {
    let timeoutId: number | undefined

    const intervalId = window.setInterval(() => {
      setIsAnimating(true)

      timeoutId = window.setTimeout(() => {
        React.startTransition(() => {
          setActiveIndex((current) => (current + 1) % clientQuestionFeed.length)
        })
        setIsAnimating(false)
      }, 340)
    }, 3800)

    return () => {
      window.clearInterval(intervalId)
      if (timeoutId !== undefined) {
        window.clearTimeout(timeoutId)
      }
    }
  }, [])

  const nextIndex = (activeIndex + 1) % clientQuestionFeed.length

  return (
    <div className="overflow-hidden rounded-[16px] bg-white/92 p-4 shadow-[inset_0_1px_0_rgba(255,255,255,0.9)]">
      <div className="relative h-[56px] overflow-hidden">
        <div
          className={cn(
            "absolute inset-0",
            isAnimating && "transition-transform duration-300 ease-[cubic-bezier(0.22,1,0.36,1)]"
          )}
          style={{
            transform: isAnimating ? "translateY(-56px)" : "translateY(0px)",
          }}
        >
          <div className="flex h-[56px] items-start">
            <p className="text-sm leading-6 text-muted-foreground">
              “{clientQuestionFeed[activeIndex]}”
            </p>
          </div>
          <div className="flex h-[56px] items-start">
            <p className="text-sm leading-6 text-muted-foreground">
              “{clientQuestionFeed[nextIndex]}”
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

function RightRailSection({
  title,
  description,
  infoTooltip,
  action,
  children,
}: {
  title: string
  description?: string
  infoTooltip?: string
  action?: React.ReactNode
  children: React.ReactNode
}) {
  return (
    <section className="border-b border-border/75 px-5 py-5 last:border-b-0">
      <div className="flex items-start justify-between gap-3">
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <h2 className="text-[14px] font-medium tracking-[-0.015em] text-foreground">
              {title}
            </h2>
            {infoTooltip ? (
              <InfoTooltip label={`About ${title}`}>{infoTooltip}</InfoTooltip>
            ) : null}
          </div>
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
