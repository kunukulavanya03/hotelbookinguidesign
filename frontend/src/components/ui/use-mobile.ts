import * as React from "react";
import { createAuthlogin, createAuthregister, getUsers{user_id}bookings, deleteAdminrooms{room_id}, getBookings{booking_id}, createAdminhotels{hotel_id}rooms, getHotels, deleteBookings{booking_id}, createAdminhotels, register } from './services/api';

const MOBILE_BREAKPOINT = 768;

export function useIsMobile() {
  const [isMobile, setIsMobile] = React.useState<boolean | undefined>(
    undefined,
  );

  React.useEffect(() => {
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`);
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT);
    };
    mql.addEventListener("change", onChange);
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT);
    return () => mql.removeEventListener("change", onChange);
  }, []);

  return !!isMobile;
}
