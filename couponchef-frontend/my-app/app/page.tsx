/**
 * v0 by Vercel.
 * @see https://v0.dev/t/cQJeAVZBHOa
 */
import Link from "next/link"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

export default function Component() {
  return (
    <div className="flex flex-col min-h-screen">
      <header className="flex items-center justify-between px-6 py-4 bg-gray-800 text-white">
        <Link className="flex items-center gap-2" href="#">
          <Package2Icon className="h-6 w-6" />
          <span className="text-lg font-semibold">CouponChef</span>
        </Link>
        <nav className="flex gap-4">
          <Link className="text-white hover:underline" href="#">
            Dashboard
          </Link>
          <Link className="text-white hover:underline" href="#">
            Settings
          </Link>
        </nav>
      </header>
      <main className="flex-1 p-6 bg-gray-100 dark:bg-gray-900">
        <div className="max-w-md mx-auto space-y-6">
          <div className="space-y-2">
            <h1 className="text-3xl font-bold">Upload Coupon Ad</h1>
            <p className="text-gray-500 dark:text-gray-400">Please upload your weekly coupon ad</p>
          </div>
          <form className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="title">Title</Label>
              <Input id="title" placeholder="Enter the title of the ad" required />
            </div>
            <div className="space-y-2">
              <Label htmlFor="date-range">Date Range</Label>
              <Input id="date-range" required type="date" />
            </div>
            <div className="space-y-2">
              <Label htmlFor="image">Image</Label>
              <Input accept="image/*" id="image" required type="file" />
            </div>
            <Button className="w-full" type="submit">
              Upload Ad
            </Button>
          </form>
          {/* <div className="border rounded-lg p-4">
            <h2 className="text-lg font-semibold">Ad Preview</h2>
            <div className="mt-4">
              <h3 className="text-xl font-bold">Ad Title</h3>
              <p className="text-gray-500 dark:text-gray-400">Ad Description</p>
              <img
                alt="Ad Image"
                className="aspect-[3/2] overflow-hidden rounded-lg object-cover mt-4"
                height="200"
                src="couponchef-frontend/my-app/app/placeholder.svg"
                width="300"
              />
            </div>
          </div> */}
        </div>
      </main>
      <footer className="flex items-center justify-center py-4 bg-gray-800 text-white">
        <p>© 2024 CouponChef Inc. All rights reserved.</p>
      </footer>
    </div>
  )
}

function Package2Icon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M3 9h18v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9Z" />
      <path d="m3 9 2.45-4.9A2 2 0 0 1 7.24 3h9.52a2 2 0 0 1 1.8 1.1L21 9" />
      <path d="M12 3v6" />
    </svg>
  )
}
