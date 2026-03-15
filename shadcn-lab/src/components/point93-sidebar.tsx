import {
  Bell,
  BrainCircuit,
  Building2,
  ChevronsUpDown,
  CircleHelp,
  FileBarChart2,
  Gauge,
  LayoutDashboard,
  Sparkles,
  Target,
} from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarRail,
} from "@/components/ui/sidebar"
import { Badge } from "@/components/ui/badge"

const productItems = [
  { label: "Dashboard", icon: LayoutDashboard, active: true },
  { label: "Assessments", icon: Target },
  { label: "Insight Areas", icon: BrainCircuit },
  { label: "Data Points", icon: Gauge },
  { label: "Scores", icon: FileBarChart2 },
  { label: "Reports", icon: Sparkles },
  { label: "Business Intelligence", icon: Building2 },
]

const adminItems = [
  { label: "AI Hub", icon: BrainCircuit },
  { label: "Graph View", icon: CircleHelp },
  { label: "Analytics", icon: FileBarChart2 },
  { label: "Feedback", icon: Bell },
]

export function Point93Sidebar() {
  return (
    <Sidebar collapsible="icon" className="border-r border-sidebar-border/70">
      <SidebarHeader className="gap-4 border-b border-sidebar-border/80 px-4 py-5">
        <div className="flex items-center gap-3">
          <div className="grid size-9 place-items-center rounded-2xl bg-sidebar-primary/12 text-sidebar-primary">
            <span className="text-lg font-semibold leading-none">93</span>
          </div>
          <div className="min-w-0 group-data-[collapsible=icon]:hidden">
            <p className="text-sm font-semibold tracking-tight">Point93</p>
            <p className="text-xs text-sidebar-foreground/65">
              Advisor intelligence
            </p>
          </div>
        </div>
        <div className="group-data-[collapsible=icon]:hidden">
          <Badge
            variant="outline"
            className="rounded-full border-sidebar-border/80 bg-white/60 px-2.5 text-[11px] text-sidebar-foreground/72"
          >
            Comprehensive plan
          </Badge>
        </div>
      </SidebarHeader>
      <SidebarContent className="px-3 py-4">
        <SidebarGroup>
          <SidebarGroupLabel>Product</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {productItems.map((item) => (
                <SidebarMenuItem key={item.label}>
                  <SidebarMenuButton
                    isActive={item.active}
                    tooltip={item.label}
                    className="h-10 rounded-xl text-[13px] font-medium"
                  >
                    <item.icon className="size-4.5 stroke-[1.9]" />
                    <span>{item.label}</span>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
        <SidebarGroup className="pt-4">
          <SidebarGroupLabel>Admin</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {adminItems.map((item) => (
                <SidebarMenuItem key={item.label}>
                  <SidebarMenuButton
                    tooltip={item.label}
                    className="h-9 rounded-xl text-[13px] font-medium text-sidebar-foreground/72"
                  >
                    <item.icon className="size-4.5 stroke-[1.8]" />
                    <span>{item.label}</span>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter className="border-t border-sidebar-border/80 px-3 py-4">
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton className="h-auto rounded-2xl px-3 py-2.5">
              <div className="grid size-8 place-items-center rounded-full bg-sidebar-primary/12 text-[12px] font-semibold text-sidebar-primary">
                AR
              </div>
              <div className="min-w-0 flex-1 group-data-[collapsible=icon]:hidden">
                <p className="truncate text-sm font-medium">Adam Rotmil</p>
                <p className="truncate text-xs text-sidebar-foreground/62">
                  admin@point93.ai
                </p>
              </div>
              <ChevronsUpDown className="ml-auto size-4 text-sidebar-foreground/55 group-data-[collapsible=icon]:hidden" />
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarFooter>
      <SidebarRail />
    </Sidebar>
  )
}
