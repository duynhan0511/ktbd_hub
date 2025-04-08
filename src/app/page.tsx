'use client'

import { useState, useEffect } from 'react'
import PlayerCard from '@/components/PlayerCard'
import { Player } from '@/types/player'
import { mockPlayers } from '@/data/mockPlayers'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import TabSelector from '@/components/TabSelector'
import SectionTitle from '@/components/SectionTitle'

export default function Home() {
  const [players, setPlayers] = useState<Player[]>([])
  const [search, setSearch] = useState<string>('')
  const [tab, setTab] = useState<string>('featured')

  useEffect(() => {
    const filtered = mockPlayers.filter(p => {
      if (tab === 'featured') return true
      return p.card_type.toLowerCase() === tab
    })
    setPlayers(filtered)
  }, [tab])

  return (
    <div className="min-h-screen bg-gradient-to-b from-[#0c0f1a] to-[#111928] text-white font-sans">
      <Header />
      <div className="absolute inset-0 -z-10 bg-gradient-to-b from-[#0c0f1a] via-[#111928] to-[#0c0f1a] opacity-80 blur-3xl"></div>

      <main className="pt-24 px-4">
        <SectionTitle title="Player of the Week" highlightColor="text-cyan-300" />
        <TabSelector tab={tab} setTab={setTab} />

        <div className="mt-8 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-6 justify-center">
          {players
            .filter(p => p.player_name.toLowerCase().includes(search.toLowerCase()))
            .map(player => (
              <PlayerCard key={player.pes_id} player={player} />
            ))}
        </div>
      </main>

      <Footer />
    </div>
  )
}
