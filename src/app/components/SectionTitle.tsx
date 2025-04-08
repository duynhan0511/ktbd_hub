'use client'

type SectionTitleProps = {
  title: string
  highlightColor?: string
}

export default function SectionTitle({ title, highlightColor = 'text-cyan-300' }: SectionTitleProps) {
  return (
    <h2 className={`text-2xl font-bold tracking-wide text-center mt-10 ${highlightColor} drop-shadow`}>
      {title}
    </h2>
  )
}
