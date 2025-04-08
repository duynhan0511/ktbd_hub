'use client'

import { Player } from '@/types/player'
import { AnimatePresence, motion } from 'framer-motion'

interface PlayerCardBackProps {
  player: Player;
  slideIndex: number;
  handleNextSlide: (e: React.MouseEvent) => void;
  handlePrevSlide: (e: React.MouseEvent) => void;
}

export default function PlayerCardBack({ player, slideIndex, handleNextSlide, handlePrevSlide }: PlayerCardBackProps) {
  return (
    <div className="relative w-full h-full rounded-lg overflow-hidden border border-pink-400 bg-black text-white p-4">
      {/* Tabs Indicator */}
      <div className="flex justify-center items-center mb-4">
        <span className={`mx-1 w-2 h-2 rounded-full ${slideIndex === 0 ? 'bg-pink-400' : 'bg-gray-600'}`}></span>
        <span className={`mx-1 w-2 h-2 rounded-full ${slideIndex === 1 ? 'bg-pink-400' : 'bg-gray-600'}`}></span>
      </div>

      {/* Slide Content with Animation */}
      <AnimatePresence mode="wait">
        {slideIndex === 0 ? (
          <motion.div
            key="stats"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: 20 }}
            transition={{ duration: 0.3 }}
            className="text-center text-xs"
          >
            <div className="grid grid-cols-2 gap-2 mb-2">
              <div>{player.stats.spd} SPD</div>
              <div>{player.stats.sho} SHO</div>
              <div>{player.stats.dri} DRI</div>
              <div>{player.stats.pas} PAS</div>
              <div>{player.stats.str} STR</div>
              <div>{player.stats.def} DEF</div>
            </div>
            <div className="text-pink-400 font-bold text-sm mt-2">{player.style}</div>
          </motion.div>
        ) : (
          <motion.div
            key="skills"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            transition={{ duration: 0.3 }}
            className="text-center text-xs"
          >
            <p className="text-pink-400 font-bold mb-2">Skills</p>
            <ul className="space-y-1">
              <li>Blocker</li>
              <li>Interception</li>
              <li>Heading</li>
              <li>Sliding Tackle</li>
              <li>Man Marking</li>
            </ul>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Navigation Arrows */}
      <div onClick={handlePrevSlide} className="absolute top-1/2 left-2 transform -translate-y-1/2 text-lg cursor-pointer">&#8592;</div>
      <div onClick={handleNextSlide} className="absolute top-1/2 right-2 transform -translate-y-1/2 text-lg cursor-pointer">&#8594;</div>
    </div>
  )
}
