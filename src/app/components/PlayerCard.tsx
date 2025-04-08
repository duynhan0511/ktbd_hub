'use client'

import { Player } from '@/types/player'

type Props = {
  player: Player
}

export default function PlayerCard({ player }: Props) {
  return (
    <div className="relative group overflow-hidden rounded-2xl p-3 border border-cyan-400 hover:shadow-neon hover:scale-105 transition-all duration-300">
      <div className="overflow-hidden rounded-xl mb-3">
        <img
          src={player.image_url}
          alt={player.player_name}
          className="w-full rounded-xl group-hover:scale-105 transition"
        />
      </div>
      <div className="text-center">
        <p className="font-bold text-sm text-cyan-300">{player.player_name}</p>
        <p className="text-xs text-pink-400 mt-1">{player.card_type} - {player.main_position}</p>
      </div>
      <div className="absolute top-2 right-3 text-lg text-pink-500 font-extrabold">
        {player.overall}
      </div>
    </div>
  )
}
