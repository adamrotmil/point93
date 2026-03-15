import * as React from "react"
import {
  ArrowRight,
  CommandIcon,
  LayoutTemplate,
  Search,
  SlidersHorizontal,
  Sparkles,
} from "lucide-react"

import { Point93DashboardPage } from "@/components/dashboard/dashboard-page"
import { SectionCard } from "@/components/dashboard/section-card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import {
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from "@/components/ui/command"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable"
import { ScrollArea } from "@/components/ui/scroll-area"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Textarea } from "@/components/ui/textarea"

const signalItems = [
  "NextGen Ready shows the strongest short-term opportunity.",
  "Client Referrals remains underdeveloped despite advisor confidence.",
  "Business Intelligence should surface two or three clearer actions.",
  "What Clients Are Asking can become a stronger premium feature.",
  "Dashboard metrics are strongest when they stay quiet and compact.",
]

export function Point93WorkbenchPage() {
  const [commandOpen, setCommandOpen] = React.useState(false)

  React.useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault()
        setCommandOpen((open) => !open)
      }
    }

    window.addEventListener("keydown", onKeyDown)
    return () => window.removeEventListener("keydown", onKeyDown)
  }, [])

  return (
    <>
      <Tabs defaultValue="dashboard" className="min-h-screen bg-background">
        <div className="sticky top-0 z-30 border-b border-border/70 bg-background/90 backdrop-blur-xl">
          <div className="mx-auto flex max-w-[1560px] flex-col gap-4 px-5 py-4 sm:px-8">
            <div className="flex flex-col gap-3 lg:flex-row lg:items-end lg:justify-between">
              <div className="space-y-1">
                <p className="text-xs font-medium tracking-[0.16em] text-muted-foreground uppercase">
                  Point93 shadcn workbench
                </p>
                <h1 className="text-[2rem] leading-none font-semibold tracking-[-0.04em] text-foreground">
                  Componentized dashboard exploration
                </h1>
                <p className="max-w-3xl text-sm leading-6 text-muted-foreground">
                  The nested shadcn sidebar is now the default Point93 shell,
                  complete with collapsible left navigation and a compactable
                  right insights rail. The component options board remains here
                  so we can evolve the system in code instead of only styling
                  captured HTML.
                </p>
              </div>
              <div className="flex flex-wrap items-center gap-2">
                <Button
                  variant="outline"
                  className="rounded-full"
                  onClick={() => setCommandOpen(true)}
                >
                  <CommandIcon className="size-4" />
                  Command menu
                </Button>
                <Dialog>
                  <DialogTrigger
                    render={<Button className="rounded-full" />}
                  >
                    <Sparkles className="size-4" />
                    Open notes panel
                  </DialogTrigger>
                  <DialogContent className="max-w-xl rounded-[28px] p-0">
                    <DialogHeader className="px-6 pt-6">
                      <DialogTitle>Design notes</DialogTitle>
                      <DialogDescription>
                        Capture what feels promising so the dashboard system can
                        evolve intentionally.
                      </DialogDescription>
                    </DialogHeader>
                    <div className="space-y-4 px-6 pb-6">
                      <Textarea
                        rows={7}
                        defaultValue="The Coinbase/Base lane feels strongest for product trust. The nested sidebar block could help us express more depth in Assessments and Results without bloating the primary dashboard."
                        className="min-h-[180px] rounded-[20px] bg-muted/35"
                      />
                    </div>
                    <DialogFooter className="rounded-b-[28px] border-t">
                      <Button variant="outline">Save draft</Button>
                      <Button>Share with team</Button>
                    </DialogFooter>
                  </DialogContent>
                </Dialog>
              </div>
            </div>
            <TabsList variant="line" className="gap-6 p-0">
              <TabsTrigger value="dashboard">
                <LayoutTemplate className="size-4" />
                Nested dashboard shell
              </TabsTrigger>
              <TabsTrigger value="library">
                <Sparkles className="size-4" />
                Component options
              </TabsTrigger>
            </TabsList>
          </div>
        </div>

        <TabsContent value="dashboard">
          <Point93DashboardPage />
        </TabsContent>
        <TabsContent value="library" className="px-5 py-6 sm:px-8 sm:py-8">
          <div className="mx-auto max-w-[1560px]">
            <ComponentOptionsBoard onOpenCommand={() => setCommandOpen(true)} />
          </div>
        </TabsContent>
      </Tabs>

      <CommandDialog
        open={commandOpen}
        onOpenChange={setCommandOpen}
        className="max-w-2xl rounded-[28px]"
      >
        <CommandInput placeholder="Search patterns, screens, and actions..." />
        <CommandList>
          <CommandEmpty>No results found.</CommandEmpty>
          <CommandGroup heading="Go to">
            <CommandItem>
              Nested dashboard shell
              <CommandShortcut>1</CommandShortcut>
            </CommandItem>
            <CommandItem>
              Component options board
              <CommandShortcut>2</CommandShortcut>
            </CommandItem>
          </CommandGroup>
          <CommandSeparator />
          <CommandGroup heading="Actions">
            <CommandItem>
              Open notes panel
              <CommandShortcut>⌘N</CommandShortcut>
            </CommandItem>
            <CommandItem>
              Compare dashboard themes
              <CommandShortcut>⌘T</CommandShortcut>
            </CommandItem>
            <CommandItem>
              Export to Figma
              <CommandShortcut>⌘E</CommandShortcut>
            </CommandItem>
          </CommandGroup>
        </CommandList>
      </CommandDialog>
    </>
  )
}

function ComponentOptionsBoard({
  onOpenCommand,
}: {
  onOpenCommand: () => void
}) {
  return (
    <div className="grid gap-6 xl:grid-cols-[minmax(0,1.15fr)_minmax(340px,0.85fr)]">
      <div className="space-y-6">
        <SectionCard
          title="Toolbar patterns"
          description="A filter and action row using shadcn primitives we can reuse across dashboard screens."
        >
          <div className="flex flex-col gap-4">
            <div className="flex flex-wrap gap-3">
              <div className="relative min-w-[260px] flex-1">
                <Search className="pointer-events-none absolute top-1/2 left-3 size-4 -translate-y-1/2 text-muted-foreground" />
                <Input
                  defaultValue="Search modules, insights, or data points"
                  className="h-11 rounded-full border-border/80 bg-white pl-9"
                />
              </div>
              <Select defaultValue="comprehensive">
                <SelectTrigger className="h-11 rounded-full border-border/80 bg-white px-4">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="comprehensive">Comprehensive</SelectItem>
                  <SelectItem value="executive">Executive</SelectItem>
                  <SelectItem value="starter">Starter</SelectItem>
                </SelectContent>
              </Select>
              <Select defaultValue="this-quarter">
                <SelectTrigger className="h-11 rounded-full border-border/80 bg-white px-4">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="this-quarter">This quarter</SelectItem>
                  <SelectItem value="this-year">This year</SelectItem>
                  <SelectItem value="all-time">All time</SelectItem>
                </SelectContent>
              </Select>
              <Button variant="outline" className="h-11 rounded-full px-4">
                <SlidersHorizontal className="size-4" />
                More filters
              </Button>
            </div>
            <div className="flex flex-wrap gap-2">
              <Badge
                variant="outline"
                className="rounded-full bg-white px-3 py-1 text-[11px]"
              >
                Search
              </Badge>
              <Badge
                variant="outline"
                className="rounded-full bg-white px-3 py-1 text-[11px]"
              >
                Select
              </Badge>
              <Badge
                variant="outline"
                className="rounded-full bg-white px-3 py-1 text-[11px]"
              >
                Command palette
              </Badge>
            </div>
          </div>
        </SectionCard>

        <SectionCard
          title="Resizable workspace"
          description="A useful pattern if we want the dashboard to hold a main canvas plus analyst notes or BI details."
        >
          <div className="h-[320px] overflow-hidden rounded-[22px] border border-border/80 bg-background">
            <ResizablePanelGroup orientation="horizontal">
              <ResizablePanel defaultSize={65} minSize={45}>
                <div className="flex h-full flex-col">
                  <div className="border-b border-border/80 px-5 py-4">
                    <p className="text-sm font-semibold text-foreground">
                      Opportunity summary
                    </p>
                    <p className="mt-1 text-sm leading-6 text-muted-foreground">
                      This panel can host charts, scorecards, or richer
                      intelligence views.
                    </p>
                  </div>
                  <div className="grid flex-1 place-items-center bg-[radial-gradient(circle_at_top,rgba(255,255,255,1),rgba(234,241,255,0.9))]">
                    <div className="text-center">
                      <p className="text-3xl font-semibold tracking-[-0.04em] text-foreground">
                        3
                      </p>
                      <p className="mt-2 text-sm text-muted-foreground">
                        high-impact opportunities identified
                      </p>
                    </div>
                  </div>
                </div>
              </ResizablePanel>
              <ResizableHandle withHandle />
              <ResizablePanel defaultSize={35} minSize={25}>
                <ScrollArea className="h-full">
                  <div className="space-y-3 p-4">
                    {signalItems.map((item) => (
                      <div
                        key={item}
                        className="rounded-[18px] border border-border/80 bg-card px-4 py-3 text-sm leading-6 text-muted-foreground"
                      >
                        {item}
                      </div>
                    ))}
                  </div>
                </ScrollArea>
              </ResizablePanel>
            </ResizablePanelGroup>
          </div>
        </SectionCard>
      </div>

      <div className="space-y-6">
        <SectionCard
          title="Operator notes"
          description="Textarea, buttons, and simple review metadata for internal collaboration."
        >
          <div className="space-y-4">
            <Textarea
              rows={8}
              defaultValue="Use the nested sidebar for deeper products like Assessments and Results. Keep the classic dashboard sidebar lighter and more summary-driven."
              className="min-h-[200px] rounded-[22px] bg-muted/35"
            />
            <div className="flex items-center justify-between gap-3">
              <div className="flex flex-wrap gap-2">
                <Badge className="rounded-full bg-primary/10 px-3 py-1 text-[11px] text-primary">
                  In review
                </Badge>
                <Badge
                  variant="outline"
                  className="rounded-full px-3 py-1 text-[11px]"
                >
                  Dashboard
                </Badge>
              </div>
              <div className="flex gap-2">
                <Button variant="outline" className="rounded-full">
                  Save draft
                </Button>
                <Button className="rounded-full">
                  Share update
                  <ArrowRight className="size-4" />
                </Button>
              </div>
            </div>
          </div>
        </SectionCard>

        <SectionCard
          title="Quick actions"
          description="Interaction components we can drop into future dashboards, detail pages, and overlays."
        >
          <div className="grid gap-3 sm:grid-cols-2">
            <Button
              variant="outline"
              className="justify-between rounded-[18px] px-4 py-6"
              onClick={onOpenCommand}
            >
              Open command palette
              <CommandIcon className="size-4" />
            </Button>
            <Dialog>
              <DialogTrigger
                render={
                  <Button
                    variant="outline"
                    className="justify-between rounded-[18px] px-4 py-6"
                  />
                }
              >
                Open decision dialog
                <ArrowRight className="size-4" />
              </DialogTrigger>
              <DialogContent className="rounded-[28px]">
                <DialogHeader>
                  <DialogTitle>Promote this pattern?</DialogTitle>
                  <DialogDescription>
                    This is the sort of lightweight confirmation or workflow
                    dialog we can reuse in the product.
                  </DialogDescription>
                </DialogHeader>
                <DialogFooter showCloseButton>
                  <Button>Promote component</Button>
                </DialogFooter>
              </DialogContent>
            </Dialog>
          </div>
        </SectionCard>
      </div>
    </div>
  )
}
