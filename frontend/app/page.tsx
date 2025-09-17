import Link from 'next/link'
import { Button } from '@/components/ui/Button'

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="max-w-2xl text-center">
        <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
          Welcome to <span className="text-primary-600">Verifly</span>
        </h1>
        <p className="mt-6 text-lg leading-8 text-gray-600">
          A secure and modern authentication platform built with Next.js and FastAPI. 
          Get started by creating an account or logging in to your existing account.
        </p>
        <div className="mt-10 flex items-center justify-center gap-x-6">
          <Link href="/auth/register">
            <Button size="lg">
              Get Started
            </Button>
          </Link>
          <Link href="/auth/login">
            <Button variant="outline" size="lg">
              Sign In
            </Button>
          </Link>
        </div>
        <div className="mt-16 flow-root sm:mt-24">
          <div className="rounded-md bg-white/5 p-2 ring-1 ring-inset ring-white/10 lg:rounded-2xl lg:p-4">
            <div className="mx-auto max-w-md rounded-lg bg-white p-6 shadow-lg">
              <div className="flex items-center space-x-3">
                <div className="h-3 w-3 rounded-full bg-green-500"></div>
                <div className="h-3 w-3 rounded-full bg-yellow-500"></div>
                <div className="h-3 w-3 rounded-full bg-red-500"></div>
              </div>
              <div className="mt-4 space-y-2">
                <div className="h-2 w-3/4 rounded bg-gray-200"></div>
                <div className="h-2 w-1/2 rounded bg-gray-200"></div>
                <div className="h-2 w-5/6 rounded bg-gray-200"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
