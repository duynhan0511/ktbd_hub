'use client'

import { Player } from '@/types/player'

type PlayerCardSimpleProps = {
  player: Player
}

export default function PlayerCardSimple({ player }: PlayerCardSimpleProps) {
  return (
    <div className="relative w-[180px] h-[260px] rounded-xl overflow-hidden border border-cyan-400 shadow-md bg-black group cursor-pointer">
      {/* Background tổng hợp mặt trước */}
      <img src={player.frontImage} alt={player.name} className="w-full h-full object-cover" />

      {/* Overlay hiệu ứng hover nhẹ */}
      <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition" />

      {/* Tên cầu thủ dưới cùng */}
      <div className="absolute bottom-2 w-full text-center text-xs font-bold text-white bg-black/50 py-1">
        {player.name}
      </div>
    </div>
  )
}
