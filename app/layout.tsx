import type {Metadata} from "next";
import "./globals.css";
export const metadata: Metadata = {title:"ClearKind — estate triage workspace",description:"A calm, deterministic first-pass estate sorting prototype."};
export default function RootLayout({children}:Readonly<{children:React.ReactNode}>){return <html lang="en"><body>{children}</body></html>}
