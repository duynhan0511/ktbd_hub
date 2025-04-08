'use client'

type TabSelectorProps = {
  tab: string
  setTab: (tab: string) => void
}

const tabs = ['featured', 'potw', 'highlight', 'legendary']

export default function TabSelector({ tab, setTab }: TabSelectorProps) {
  return (
    <div className="flex flex-wrap justify-center gap-2 mt-4">
      {tabs.map((key) => (
        <button
          key={key}
          onClick={() => setTab(key)}
          className={`px-4 py-2 rounded-full text-xs uppercase font-semibold border transition ${
            tab === key
              ? 'bg-pink-500 text-white'
              : 'border-pink-400 text-pink-400 hover:bg-pink-500 hover:text-white'
          }`}
        >
          {key}
        </button>
      ))}
    </div>
  )
}
