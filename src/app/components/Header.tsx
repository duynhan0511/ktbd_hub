'use client'

export default function Header() {
  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-[#0c0f1a]/80 backdrop-blur border-b border-cyan-500 flex justify-between items-center px-6 py-4">
      <h1 className="text-2xl font-bold tracking-wider text-cyan-400 drop-shadow">
        eFootballDB Vietnam
      </h1>
      <nav className="space-x-6 text-sm">
        <a href="/" className="hover:text-pink-400 transition">Home</a>
        <a href="/players" className="hover:text-pink-400 transition">Players</a>
        <a href="/teams" className="hover:text-pink-400 transition">Teams</a>
      </nav>
    </header>
  )
}
