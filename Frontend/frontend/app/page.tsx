import React, { useState, useContext, useEffect } from "react";
import { useRouter } from "next/router";
import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-4xl font-bold">Welcome to Our Home Page</h1>
      <p className="text-lg mt-4">
      <Link href="/login">
        <div className="shadow-md border border-gray-300 p-6 rounded-lg hover:bg-gray-50">
          Login</div>
      </Link>
      </p>
      <p className="text-lg mt-4">
      <Link href="/register">
        <div className="shadow-md border border-gray-300 p-6 rounded-lg hover:bg-gray-50">
          Create an account</div>
      </Link>
      </p>
    </div>
  );
}