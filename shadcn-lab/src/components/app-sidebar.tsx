import * as React from "react"

import { NavMain } from "@/components/nav-main"
import { NavProjects } from "@/components/nav-projects"
import { NavUser } from "@/components/nav-user"
import { TeamSwitcher } from "@/components/team-switcher"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarRail,
} from "@/components/ui/sidebar"
import {
  BarChart3Icon,
  BrainCircuitIcon,
  Building2Icon,
  FileBarChart2Icon,
  GaugeIcon,
  LayoutDashboardIcon,
  RadarIcon,
  SparklesIcon,
  TargetIcon,
  WorkflowIcon,
} from "lucide-react"

const data = {
  user: {
    name: "Adam Rotmil",
    email: "admin@point93.ai",
    avatar: "",
  },
  teams: [
    {
      name: "Point93",
      logo: <WorkflowIcon />,
      plan: "Comprehensive",
    },
    {
      name: "Executive",
      logo: <SparklesIcon />,
      plan: "Advisory",
    },
    {
      name: "Corporate",
      logo: <Building2Icon />,
      plan: "Enterprise",
    },
  ],
  navMain: [
    {
      title: "Dashboard",
      url: "#",
      icon: <LayoutDashboardIcon />,
      isActive: true,
      items: [
        {
          title: "Overview",
          url: "#",
        },
        {
          title: "Advisor score",
          url: "#",
        },
        {
          title: "Signals",
          url: "#",
        },
      ],
    },
    {
      title: "Assessments",
      url: "#",
      icon: <TargetIcon />,
      items: [
        {
          title: "My journey",
          url: "#",
        },
        {
          title: "Current module",
          url: "#",
        },
        {
          title: "Completed modules",
          url: "#",
        },
      ],
    },
    {
      title: "Results",
      url: "#",
      icon: <RadarIcon />,
      items: [
        {
          title: "Scores",
          url: "#",
        },
        {
          title: "Insight areas",
          url: "#",
        },
        {
          title: "Data points",
          url: "#",
        },
        {
          title: "Reports",
          url: "#",
        },
      ],
    },
    {
      title: "Business Intelligence",
      url: "#",
      icon: <BrainCircuitIcon />,
      items: [
        {
          title: "Opportunity library",
          url: "#",
        },
        {
          title: "Priorities",
          url: "#",
        },
        {
          title: "Profile signals",
          url: "#",
        },
        {
          title: "What clients ask",
          url: "#",
        },
      ],
    },
  ],
  projects: [
    {
      name: "Advisor Profiles",
      url: "#",
      icon: <GaugeIcon />,
    },
    {
      name: "Performance Benchmarks",
      url: "#",
      icon: <BarChart3Icon />,
    },
    {
      name: "BI Modules",
      url: "#",
      icon: <FileBarChart2Icon />,
    },
  ],
}

export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
  return (
    <Sidebar
      collapsible="icon"
      className="border-r border-sidebar-border/80"
      {...props}
    >
      <SidebarHeader>
        <TeamSwitcher teams={data.teams} />
      </SidebarHeader>
      <SidebarContent>
        <NavMain items={data.navMain} />
        <NavProjects projects={data.projects} />
      </SidebarContent>
      <SidebarFooter>
        <NavUser user={data.user} />
      </SidebarFooter>
      <SidebarRail />
    </Sidebar>
  )
}
