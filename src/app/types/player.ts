export type Player = {
  id: string;
  name: string;
  position: string;
  overall: number;
  frontImage: string;
  clubLogo: string;
  playerFace: string;
  stats: {
    spd: number;
    sho: number;
    dri: number;
    pas: number;
    str: number;
    def: number;
  };
  style: string;
  card_type: string;
}