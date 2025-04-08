'use client'

import { useState } from 'react'
import PlayerCardFront from './PlayerCardFront'
import PlayerCardBack from './PlayerCardBack'
import { Player } from '@/types/player'

type PlayerCardFlipProps = {
  player: Player
}

export default function PlayerCardFlip({ player }: PlayerCardFlipProps) {
  const [flipped, setFlipped] = useState(false)

  return (
    <div className="w-[180px] h-[260px] perspective cursor-pointer" onClick={() => setFlipped(!flipped)}>
      <div className={`relative w-full h-full transition-transform duration-700 transform-style-preserve-3d ${flipped ? 'rotate-y-180' : ''}`}>
        {/* Front Side */}
        <div className="absolute w-full h-full backface-hidden">
          <PlayerCardFront player={player} />
        </div>

        {/* Back Side */}
        <div className="absolute w-full h-full backface-hidden rotate-y-180">
          <PlayerCardBack player={player} />
        </div>
      </div>
    </div>
  )
}
