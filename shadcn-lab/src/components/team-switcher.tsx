import {
  SidebarMenu,
  SidebarMenuItem,
  useSidebar,
} from "@/components/ui/sidebar"

export function TeamSwitcher({ plan }: { plan: string }) {
  const { state } = useSidebar()
  const collapsed = state === "collapsed"
  const logoSrc = `${import.meta.env.BASE_URL}p93-logo-spread.png`

  return (
    <SidebarMenu>
      <SidebarMenuItem>
        {collapsed ? (
          <div className="mx-auto flex size-9 items-center justify-center rounded-xl bg-sidebar-accent text-[11px] font-semibold tracking-[0.14em] text-sidebar-foreground">
            P93
          </div>
        ) : (
          <div className="px-1 py-1">
            <img
              src={logoSrc}
              alt="Point93"
              className="h-[18px] w-auto object-contain"
            />
            <span className="mt-2 inline-flex rounded-full border border-sidebar-border bg-secondary px-2.5 py-1 text-[10px] font-medium text-muted-foreground">
              {plan}
            </span>
          </div>
        )}
      </SidebarMenuItem>
    </SidebarMenu>
  )
}
