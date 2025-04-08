'use client'

import { Player } from '@/types/player'

type PlayerCardFrontProps = {
  player: Player
}

export default function PlayerCardFront({ player }: PlayerCardFrontProps) {
  return (
    <div className="relative w-full h-full rounded-lg overflow-hidden border border-cyan-400 bg-black">
      {/* Background tổng hợp mặt trước */}
      <img src={player.frontImage} alt="Card Background" className="w-full h-full object-cover" />

      {/* Overall + Position */}
      <div className="absolute top-2 left-2 text-white text-xs font-bold">
        <div className="text-2xl leading-5">{player.overall}</div>
        <div className="text-sm">{player.position}</div>
      </div>

      {/* Club logo */}
      <div className="absolute top-2 right-2 w-8 h-8">
        <img src={player.clubLogo} alt="Club Logo" className="w-full h-full object-contain" />
      </div>

      {/* Player Face */}
      <div className="absolute inset-0 flex items-center justify-center">
        <img src={player.playerFace} alt="Player Face" className="w-24 h-24 object-contain" />
      </div>

      {/* Player Name */}
      <div className="absolute bottom-10 w-full text-center text-white text-sm font-bold">
        {player.name}
      </div>

      {/* Stars (mock cố định) */}
      <div className="absolute bottom-5 w-full text-center text-yellow-400 text-xs">
        ★★★★★
      </div>
    </div>
  )
}
