"use client"

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
} from "@/components/ui/sidebar"
import { ChevronRightIcon } from "lucide-react"

export function NavMain({
  items,
  label,
}: {
  items: {
    title: string
    url: string
    icon?: React.ReactNode
    isActive?: boolean
    tooltip?: string
    collapsible?: boolean
    defaultOpen?: boolean
    badge?: string | number
    emptyLabel?: string
    items?: {
      title: string
      url: string
    }[]
  }[]
  label?: string
}) {
  return (
    <SidebarGroup>
      {label ? <SidebarGroupLabel>{label}</SidebarGroupLabel> : null}
      <SidebarMenu>
        {items.map((item) => (
          item.collapsible ? (
            <Collapsible
              key={item.title}
              defaultOpen={item.defaultOpen ?? item.isActive}
              className="group/collapsible"
              render={<SidebarMenuItem />}
            >
              <CollapsibleTrigger
                render={
                  <SidebarMenuButton
                    tooltip={item.tooltip ?? item.title}
                    className="h-10 rounded-xl px-3 text-[14px] font-medium text-sidebar-foreground/88 [&_svg]:size-[18px]"
                  />
                }
              >
                {item.icon}
                <span>{item.title}</span>
                {item.badge ? (
                  <span className="ml-auto inline-flex min-w-7 items-center justify-center rounded-md bg-primary/20 px-2 py-1 text-[11px] font-medium leading-none text-primary">
                    {item.badge}
                  </span>
                ) : null}
                <ChevronRightIcon className="ml-auto transition-transform duration-200 group-data-open/collapsible:rotate-90" />
              </CollapsibleTrigger>
              <CollapsibleContent>
                {item.items?.length ? (
                  <SidebarMenuSub className="ml-4 border-l border-sidebar-border/65 pl-2.5">
                    {item.items.map((subItem) => (
                      <SidebarMenuSubItem key={subItem.title}>
                        <SidebarMenuSubButton
                          className="h-auto min-h-8 items-start gap-3 rounded-lg px-2 py-2 text-[13px] leading-[1.34] text-sidebar-foreground/66 hover:bg-transparent hover:text-sidebar-foreground/88"
                          render={<a href={subItem.url} />}
                        >
                          <span className="mt-[0.44rem] size-1 shrink-0 rounded-full bg-sidebar-foreground/28" />
                          <span className="whitespace-normal">{subItem.title}</span>
                        </SidebarMenuSubButton>
                      </SidebarMenuSubItem>
                    ))}
                  </SidebarMenuSub>
                ) : (
                  <div className="ml-9 px-2 py-2 text-[12px] italic text-sidebar-foreground/48">
                    {item.emptyLabel ?? "No items available"}
                  </div>
                )}
              </CollapsibleContent>
            </Collapsible>
          ) : (
            <SidebarMenuItem key={item.title}>
              <SidebarMenuButton
                tooltip={item.tooltip ?? item.title}
                isActive={item.isActive}
                className="h-10 rounded-xl px-3 text-[14px] font-medium text-sidebar-foreground/88 [&_svg]:size-[18px]"
                render={<a href={item.url} />}
              >
                {item.icon}
                <span>{item.title}</span>
              </SidebarMenuButton>
            </SidebarMenuItem>
          )
        ))}
      </SidebarMenu>
    </SidebarGroup>
  )
}
