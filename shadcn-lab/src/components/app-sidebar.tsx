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
  BrainIcon,
  ChartColumnBigIcon,
  DatabaseIcon,
  FileTextIcon,
  HouseIcon,
  LayoutGridIcon,
  LightbulbIcon,
  MessageSquareMoreIcon,
  NetworkIcon,
  SparklesIcon,
  UsersIcon,
} from "lucide-react"

const data = {
  user: {
    name: "Brendon Smith",
    email: "admin@point93.ai",
    avatar: "",
  },
  plan: "Comprehensive",
  navMain: [
    {
      title: "Dashboard",
      url: "#",
      icon: <HouseIcon />,
      isActive: true,
    },
    {
      title: "Assessments",
      url: "#",
      icon: <ChartColumnBigIcon />,
      collapsible: true,
      defaultOpen: true,
      badge: 6,
      items: [
        {
          title: "View All",
          url: "#",
        },
        {
          title: "Your Professional Foundation & Team Structure",
          url: "#",
        },
        {
          title: "Your Firm Platform, Technology & Support",
          url: "#",
        },
        {
          title: "Your Investment Management Excellence",
          url: "#",
        },
        {
          title: "Your Planning Process & Implementation",
          url: "#",
        },
        {
          title: "Your Client Service & Communication",
          url: "#",
        },
        {
          title: "Your Fees, Value & Positioning",
          url: "#",
        },
      ],
    },
    {
      title: "Insight Areas",
      url: "#",
      icon: <SparklesIcon />,
    },
    {
      title: "Data Points",
      url: "#",
      icon: <DatabaseIcon />,
    },
    {
      title: "Scores",
      url: "#",
      icon: <BarChart3Icon />,
    },
    {
      title: "Reports",
      url: "#",
      icon: <FileTextIcon />,
    },
    {
      title: "Business Intelligence",
      url: "#",
      icon: <LightbulbIcon />,
      collapsible: true,
      defaultOpen: true,
      badge: 5,
      items: [
        {
          title: "View All",
          url: "#",
        },
        {
          title: "NextGen Ready",
          url: "#",
        },
        {
          title: "Client Referrals",
          url: "#",
        },
        {
          title: "PitchPerfect",
          url: "#",
        },
        {
          title: "COI Referrals",
          url: "#",
        },
        {
          title: "Client Retention Risk",
          url: "#",
        },
      ],
    },
  ],
  projects: [
    {
      name: "Area Builder",
      url: "#",
      icon: <LayoutGridIcon />,
    },
    {
      name: "BI Builder",
      url: "#",
      icon: <LightbulbIcon />,
    },
    {
      name: "AI Hub",
      url: "#",
      icon: <BrainIcon />,
    },
    {
      name: "Graph View",
      url: "#",
      icon: <NetworkIcon />,
    },
    {
      name: "User Management",
      url: "#",
      icon: <UsersIcon />,
    },
    {
      name: "Analytics",
      url: "#",
      icon: <BarChart3Icon />,
    },
    {
      name: "Feedback",
      url: "#",
      icon: <MessageSquareMoreIcon />,
    },
    {
      name: "Beta",
      url: "#",
      icon: <SparklesIcon />,
    },
  ],
}

export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
  return (
    <Sidebar
      collapsible="icon"
      className="border-r border-sidebar-border bg-sidebar"
      {...props}
    >
      <SidebarHeader className="border-b border-sidebar-border/80 px-4 py-4">
        <TeamSwitcher plan={data.plan} />
      </SidebarHeader>
      <SidebarContent>
        <NavMain items={data.navMain} />
        <NavProjects projects={data.projects} title="Admin" />
      </SidebarContent>
      <SidebarFooter>
        <NavUser user={data.user} />
      </SidebarFooter>
      <SidebarRail />
    </Sidebar>
  )
}
